from django.shortcuts import render

from .carro import Carro

from tienda.models import Producto

from django.shortcuts import redirect

from django.core.mail import EmailMessage

# Create your views here.

def agregar_producto(request, producto_id):

    carro=Carro(request)#creo objeto tipo carro

    producto=Producto.objects.get(id=producto_id)#obtengo el producto

    carro.agregar(producto=producto)

    return redirect('Tienda') #para refrescar la pagina

def eliminar_producto(request, producto_id):

    carro=Carro(request)#creo objeto tipo carro

    producto=Producto.objects.get(id=producto_id)#obtengo el producto

    carro.eliminar(producto=producto)

    return redirect('Tienda') #para refrescar la pagina

def restar_producto(request, producto_id):

    carro=Carro(request)#creo objeto tipo carro

    producto=Producto.objects.get(id=producto_id)#obtengo el producto

    carro.restar_producto(producto=producto)

    return redirect('Tienda') #para refrescar la pagina

def limpiar_carro(request):

    carro=Carro(request)#creo objeto tipo carro

    carro.limpiar_carro()

    return redirect('Tienda') #para refrescar la pagina

def comprar_producto(request):  #función que envia mails, colocar mail correspondiente al que vas a utilizar (normalmente el que se coloco en el settings.py)


    userEmail=request.user.email
    userName=request.user.username
    
    for key, value in request.session.items():
        print('la llave es {} el valor es => {}'.format(key,value))
        
        if  key=="carro" :
            
            miEmail=EmailMessage('Mensaje de compra de mi app DJANGO', 'El Usuario con nombre {} con la dirección  {} quiere lo siguiente:\n\n {}'.format(userName,userEmail,value),
            '', ['TUMAIL@gmail.com'], reply_to=[userEmail])
            try:
                miEmail.send()
                return redirect('/tienda/?enviado')
            except:
                return redirect('/tienda/?noEnviado')

        
    
        
    