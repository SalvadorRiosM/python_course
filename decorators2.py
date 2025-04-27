def announce(function_inside):                #    (anuncio)
    def wrapper():              #    (envoltura)
        print("About to run the function...")
        function_inside()                    
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello, World!")

@announce    
def name():
    print("My name is Orlandito")
    
hello()
name()
