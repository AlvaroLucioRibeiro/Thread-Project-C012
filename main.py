from threading import Thread
from car import Car

cars = []

winners = []

car1 = Car("Barão Vermelho", 5)
car2 = Car("Penelope", 5)
car3 = Car("Irmãos Rocha", 5)
car4 = Car("Dick Vigarista", 5)
car5 = Car("Dupla Sinistra", 5)
car6 = Car("Professor Aéreo", 5)
car7 = Car("Tomas e Urso", 5)
car8 = Car("Peter Perfeito", 5)
car9 = Car("Meekley", 5)
car10 = Car("Quadrilha da Morte", 5)

cars = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10]

for car in cars:
  car.start()

for car in cars:
  car.join()

print(Car.winners)

for car in cars:
  print(f"{car.name}: {car.num_of_pauses}")
