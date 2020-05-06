# Este formulario lo manda a llamar la vista para renderizar
# La plantilla va a mostrar lo que se especifica aca

from django import forms


from .models import ResPartner

class ClientesForm(forms.ModelForm):
    class Meta:
        model = ResPartner
        fields = ['name',
                  'street',
                  'city',
                  'zip',
                  'phone',
                  'mobile',
                  'email',
                  'main_id_category',
                  'main_id_number',
                  'afip_responsability_type',
                  'x_tc_visa'
                  ]

        labels = {'name':'Nombre del cliente', 
                  'ref':'Codigo de cliente',
                  'street':'Dirección',
                  'city':'Ciudad',
                  'zip':'Código Postal',
                  'phone':'Telefono',
                  'mobile':'Celular',
                  'email':'Dirección de correo'
                  }

        widget = {'name':forms.TextInput,
                  'ref':forms.TextInput,
                  'street':forms.TextInput,
                  'city':forms.TextInput,
                  'zip':forms.TextInput,
                  'phone':forms.TextInput,
                  'mobile':forms.TextInput,
                  'email':forms.EmailInput,
                  'main_id_category':forms.TextInput,
                  'main_id_number':forms.TextInput,
                  'afip_responsability_type':forms.TextInput,
                  'x_tc_visa':forms.TextInput
                  } # especificamos en los widget los tipos input HTML 
                                                                # que van a utilizar los campos de formularios que se van a renderizar

    # sobreescribo el metodo init de este formulario para renderizar con bootstrap
    def __init__(self, *args, **kwargs): # con esto garantizamos que al iniciar la clase reescribimos su propio metodo de inicio
        super().__init__(*args,**kwargs) # invoco al init de la funcion padre
        for field in iter(self.fields): # recorremos todos los campos que se van a mostrar
            self.fields[field].widget.attrs.update({ # a cada campo que va iterando le va a asignar un widget
                'class':'form-control'
            }) 
