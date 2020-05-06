from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import F, Sum
from django.db.models.functions import Round


from interfaces.models import ResPartner, AccountInvoice
from interfaces.forms import ClientesForm
from interfaces.gateway815 import ochoquince

# from django.http import HttpResponse

# from interfaces.gateway815 import ochoquince
# from interfaces.odoo import fnOdoo,Odoo

# Create your views here.

class ClientesOdooView(LoginRequiredMixin,generic.ListView):
    model = ResPartner
    queryset = ResPartner.objects.filter(customer=True, employee=False)
    template_name = "interfaces/clientes_list.html"
    context_object_name = "obj" # renombramos el nombre del objeto para tener mas control. Por defecto Django lo llama "object"
    login_url = "bases:login" # definimos la url de login por si no lo estuvieramos

class ClientesOdooNew(LoginRequiredMixin,generic.CreateView):
    model=ResPartner
    template_name = "interfaces/clientes_form.html"
    context_object_name = "obj"
    form_class = ClientesForm
    success_url = reverse_lazy("interfaces:clientes_list")
    success_message="Cliente creado satisfactoriamente"
    login_url="bases:login"
    
    def form_valid(self, form):  # sobreescribimos este metodo para enviarle el token id del usuario logueado
        form.instance.uc = self.request.user # tomamos el usuario loqueado y se lo mandamos a la instancia
        return super().form_valid(form) # si esta validado retornamos y sobreescribimos la propiedad form_valid del padre con el formulario modificado

class ClientesOdooEdit(LoginRequiredMixin,generic.UpdateView):
    model=ResPartner
    template_name = "interfaces/clientes_form.html"
    context_object_name = "obj"
    form_class = ClientesForm
    success_url = reverse_lazy("interfaces:clientes_list")
    success_message="Cliente actualizado satisfactoriamente"
    login_url="bases:login"
    
    def form_valid(self, form):  # sobreescribimos este metodo para enviarle el token id del usuario logueado
        form.instance.um = self.request.user.id # tomamos el usuario loqueado y se lo mandamos a la instancia
        return super().form_valid(form) # si esta validado retornamos y sobreescribimos la propiedad form_valid del padre con el formulario modificado


# class DeudaVencidaClientesView(LoginRequiredMixin,generic.ListView):
#     model = AccountInvoice
#     queryset = AccountInvoice.objects.filter(state='open', journal_id=11).aggregate(sum=Round(Sum(F('residual'))))
#     template_name = "interfaces/dashboard.html"
#     context_object_name = "obj" # renombramos el nombre del objeto para tener mas control. Por defecto Django lo llama "object"
#     login_url = "bases:login" # definimos la url de login por si no lo estuvieramos

class dashboard(LoginRequiredMixin):

    def DeudaVencidaClientesView(request):
        model = AccountInvoice
        deuda = AccountInvoice.objects.filter(state='open', journal_id=11).aggregate(sum=Round(Sum(F('residual'))))
        template_name = "interfaces/dashboard.html"
        # context_object_name = "obj" # renombramos el nombre del objeto para tener mas control. Por defecto Django lo llama "object"
        # login_url = "bases:login" # definimos la url de login por si no lo estuvieramos
        return render(request,template_name,{'obj': deuda})


class DeudaVencidaClientesDetalleView(LoginRequiredMixin,generic.ListView):
    # model = AccountInvoice.objects.annotate(deuda=Sum(F('residual'))).filter(state='open', journal_id=11)
    model = AccountInvoice
    queryset = AccountInvoice.objects.filter(state='open', journal_id=11).values('partner_id__ref', 'partner_id__name','partner_id__phone','partner_id__mobile').annotate(deuda=Round(Sum(F('residual'))))
    # queryset = AccountInvoice.objects.filter(state='open', journal_id=11).values('partner_id').annotate(sum=Round(Sum(F('residual'))))
    template_name = "interfaces/clientes_deuda.html"
    context_object_name = "obj" # renombramos el nombre del objeto para tener mas control. Por defecto Django lo llama "object"
    login_url = "bases:login" # definimos la url de login por si no lo estuvieramos    

# class ClientesOchoquinceView(LoginRequiredMixin):
class ClientesOchoquinceView():
    
    def buscarClientes(request):
        gw=ochoquince()
        token=gw.obtenerToken()
        listaClientes = gw.obtenerClientes(token)
     
        template_name = "interfaces/clientes_gw_list.html"
        return render(request,template_name,{'cliente': listaClientes})

    def integraCliente(request):
        gw=ochoquince()
        token=gw.obtenerToken()
        listaCliGW = gw.obtenerClientes(token)
        listaCliOdoo = ResPartner.objects.filter(customer=True, parent_id=None)
        listaClientes=[]

        for cliOdoo in listaCliOdoo:

            for cliGW in listaCliGW:

                if cliOdoo.ref == cliGW[4] and (cliOdoo.ref != None or cliGW[4] != None):
                    listaClientes.append([cliOdoo.ref,cliOdoo.name,cliGW[1],cliGW[0]])   
                    break
        
        for cliOdoo in listaCliOdoo:
            if cliOdoo.ref == None:
                listaClientes.append(['Falta NroCliente Odoo',cliOdoo.name,'','']) 

        for cliGW in listaCliGW:
            if cliGW[4] == None:
                listaClientes.append(['Falta Conector GW','',cliGW[1],cliGW[0]])  
        
      
        template_name = "interfaces/clientes_integracli_list.html"
        return render(request,template_name,{'cliente': listaClientes})
