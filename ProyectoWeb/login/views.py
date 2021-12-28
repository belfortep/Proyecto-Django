from django.shortcuts import render, redirect

from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.


def login(request):

    formulario_login=UserRegisterForm()
    return render(request, 'login/login.html', {'form' : formulario_login})

def register(request):

    if request.method=='POST':
        formulario_registrar=UserRegisterForm(request.POST)
        if formulario_registrar.is_valid():
            formulario_registrar.save()
            username = formulario_registrar.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('/login/login')
            
        
    else:
        formulario_registrar = UserRegisterForm()

    

    return render(request, 'login/register.html', {'form' : formulario_registrar})
    


