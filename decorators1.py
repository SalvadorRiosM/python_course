def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        print("Vamnos a realizar un calculo")
        funcion_parametro()
        print("Hemos terminado el calculo")
    return funcion_interior
    
@funcion_decoradora
def suma():
    print(15 + 15)
@funcion_decoradora  
def resta():
    print(20 - 15)

 
suma()
resta()