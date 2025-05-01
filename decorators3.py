def decorador(f):
    def encapsulado():
        print("Primer comentario")
        f()
        print("Segundo comentario")
        return encapsulado
    
@decorador                          # El decorador va arriba de "lA FUNCION" que quieres decorar
def comentario():
    print("Imprime algo")


comentario()
            
        
        