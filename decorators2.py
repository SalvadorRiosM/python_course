def announce(interior):                # (anuncio) la funcion decoradora toma como parametro la funcion interior
    def wrapper():                     # (envoltura)
        print("About to run the function...")
        interior()                    
        print("Done function.")
    return wrapper

@announce    
def name():
    print("My name is Orlandito")
    
name()
