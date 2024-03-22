from time import sleep
from car import Car
from random import randint
import os

persons = ["Barão Vermelho", "Penelope", "Irmãos Rocha", "Dick Vigarista", "Dupla Sinistra", "Professor Aéreo", "Tomas e Urso", "Peter Perfeito", "Meekley", "Quadrilha da Morte"]
colors = ["#FF7F50", "#48D1CC", "#DB7093", "#1E90FF", "#D2691E", "#87CEEB", "#DAA520", "#98FB98", "#3CB371", "#008B8B"]
cars = []

color = 0
for person in persons:
  speed = randint(5, 10)
  cars.append(Car(person, speed, colors[color]))
  color += 1

print("\n############ A CORRIDA VAI COMEÇAR ############\n")
print("-----------CORREDORES-----------")

for car in cars:
  print(f"{car.name} -> velocidade: {car.speed}")

sleep(5)
os.system('cls')
  
for car in cars:
  car.start()

for car in cars:
  car.join()

os.system('cls')

print("-----------RESULTADO-----------")
for c in Car.winners:
  print(f"{Car.winners[c]}º lugar: {c}")