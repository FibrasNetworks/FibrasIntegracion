from django.urls import path
from interfaces.views import ClientesOdooView, ClientesOdooNew, ClientesOdooEdit,\
    ClientesOchoquinceView, dashboard,DeudaVencidaClientesDetalleView

urlpatterns = [

    path('clientes/', ClientesOdooView.as_view(), name="clientes_list"),
    path('clientes/new', ClientesOdooNew.as_view(), name="cliente_new"),
    path('clientes/edit/<int:pk>', ClientesOdooEdit.as_view(), name="clientes_edit"),

    path('clientes/gateway', ClientesOchoquinceView.buscarClientes, name='clientes_list_gateway'),
    path('clientes/integra', ClientesOchoquinceView.integraCliente, name='clientes_list_integra'),
    path('clientes/clideuda', DeudaVencidaClientesDetalleView.as_view(), name='clientes_deuda'),
        
    # path('administracion/dashboard', DeudaVencidaClientesView.as_view(), name="dashboard_deuda_vencida"),
    path('administracion/dashboard', dashboard.DeudaVencidaClientesView, name="dashboard_deuda_vencida"),
    

    # path('buscar/', views.buscar),
    # path('gw815/', views.gw815),
    # path('cliodoo', views.lista_cliente_odoo),

]