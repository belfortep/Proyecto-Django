from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):

    formulario_contacto=FormularioContacto()

    if request.method=='POST':
        formulario_contacto=FormularioContacto(data=request.POST)#cargar en formulario la informacion que coloco el usuario y aca la rescato
        if formulario_contacto.is_valid():
            nombre=request.POST.get('nombre')
            email=request.POST.get('email')
            contenido=request.POST.get('contenido')
            
            

            miEmail=EmailMessage('Mensaje desde mi app Django', 'El Usuario con nombre {} con la dirección  {} escribe lo siguiente:\n\n {}'.format(nombre,email,contenido),
            '', ['TUMAIL@gmail.com'], reply_to=[email])

            try:
                miEmail.send()

                return redirect('/contacto/?valido') #me redirecciona a la misma pagina, pero con un parametro que dice valido. Se usa en el template

            except:
                return redirect('/contacto/?novalido')

    return render(request, 'contacto/contacto.html', {'miFormulario' : formulario_contacto})
