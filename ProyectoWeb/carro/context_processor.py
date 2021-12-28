from .carro import Carro
def importe_total_carro(request):
    total=0
    miCarro=Carro(request)  #debo crear el objeto Carro aunque no lo use aca para poder acceder a el, si no, no funciona NADA del sitio web
    
    try:
        if request.user.is_authenticated:
        
            for key, value in request.session.items():
                print('{} => {}'.format(key,value))

            for key,value in request.session['carro'].items():

                key
                total= total + (float(value['precio']))

            return {'importe_total_carro':total}
    
        print('XD')
        return {'importe_total_carro':total}
    except:
        return {'importe_total_carro':total}
        
        



#CONTEXT_PROCESSOR, CREA VARIABLES GLOBALES. hay que ir al settings, templates donde pone context_processor y colocar el mio