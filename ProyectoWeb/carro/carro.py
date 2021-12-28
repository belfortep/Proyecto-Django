

class Carro:
    def __init__(self, request):
        self.request=request                #peticion request almacenada
        self.session=request.session        #sesion almacenada
        carro=self.session.get('carro')     #se identifica con el string carro

        if not carro: #creando el carrito de la compra
            carro=self.session['carro']={}  #en definitiva, el carro es un diccionario que tiene el id como clave, y el valor es un diccionario con las caracteristicas de esa id
        
        self.carro=carro        #si ya existe carro (sesion abierta de antes), se guarda el carro asi no se pierde info

    def agregar(self,producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                'producto_id':producto.id,
                'nombre':producto.nombre,
                'precio':str(producto.precio),
                'cantidad':1,
                'imagen':producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value['cantidad']=value['cantidad']+1
                    value['precio']=float(value['precio'])+producto.precio
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session['carro']=self.carro    #el carro que esta en la session, debe ser igual al carro
        self.session.modified=True

    def eliminar(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar_producto(self, producto):
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value['cantidad']=value['cantidad']-1
                    value['precio']=float(value['precio'])-producto.precio
                    if value['cantidad']<1:
                        self.eliminar(producto)
                    break
            self.guardar_carro()

    def limpiar_carro(self):
        self.session['carro']={}
        self.session.modified=True

    

