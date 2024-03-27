from time import sleep
from car import Car
from random import randint
import os

# Lista de nomes dos participantes da corrida
persons = ["Barão Vermelho", "Penelope", "Irmãos Rocha", "Dick Vigarista", "Dupla Sinistra", "Professor Aéreo", "Tomas e Urso", "Peter Perfeito", "Meekley", "Quadrilha da Morte"]

# Lista de cores associadas a cada participante para uso na interface gráfica da corrida
colors = ["#FF7F50", "#48D1CC", "#DB7093", "#1E90FF", "#D2691E", "#87CEEB", "#DAA520", "#98FB98", "#3CB371", "#008B8B"]
cars = []  # Lista para armazenar os objetos Car criados para cada participante

color = 0  # Índice para acessar a lista de cores

for person in persons:
  speed = randint(5, 10)  # Gera uma velocidade aleatória para cada carro entre 5 e 10
  cars.append(Car(person, speed, colors[color]))  # Cria um objeto Car e o adiciona à lista de carros
  color += 1  # Incrementa o índice de cores para usar a próxima cor disponível

print("\n############ A CORRIDA VAI COMEÇAR ############\n")
print("-----------CORREDORES-----------")

# Exibe os nomes e velocidades dos carros participantes
for car in cars:
  print(f"{car.name} -> velocidade: {car.speed}")

sleep(5)  # Aguarda 5 segundos antes de começar a corrida
os.system("cls")  # Limpa a tela do terminal para iniciar a corrida
  
# Inicia a thread de cada carro, começando a corrida
for car in cars:
  car.start()

# Aguarda a finalização de todas as threads dos carros
for car in cars:
  car.join()

os.system('cls')  # Limpa a tela do terminal para mostrar os resultados

print("-----------RESULTADO-----------")
# Exibe o resultado da corrida com a posição e nome de cada carro
for c in Car.winners:
  print(f"{Car.winners[c]}º lugar: {c}")