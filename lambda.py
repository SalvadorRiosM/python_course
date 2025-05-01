people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},              # Diccionario dentro de una lista
    {"name": "Draco", "house": "Slytherin"}
]

def funcion(person):
    return person["house"]

people.sort(key=funcion)
print(people)


