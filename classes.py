class Flight():
    def __init__(self, capacity):
        self.capacidad = capacity
        self.passengers = []
        
    def add_passengers(self, name):
        if not self.open_seats():          # Esto es lo mismo que: if self.open_seats == 0 ():
            return False
        self.passengers.append(name)
        return True
        
    def open_seats(self):
        return self.capacidad - len(self.passengers)
        
avion1 = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]

for person in people:
    success = avion1.add_passengers(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No avaible seats for {person}")
        

    