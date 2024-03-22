from random import randint
from time import sleep
from threading import Thread
import os

class Car(Thread):
  winners = []

  def __init__(self, name, speed):
    super().__init__()
    self.name = name
    self.speed = speed
    self.displacement = 0
    self.num_of_pauses = 0

  def run(self):

    while self.displacement < 100:
      self.displacement += self.speed

      if randint(1, 10) == 7:
        print(f"{self.name}: Tomou pau de 1 sec\n")
        self.num_of_pauses += 1
        sleep(6)

      print(f"The {self.name} is in {self.displacement} position")

      # Time between each 100m
      sleep(2)
      os.system('c')

    Car.winners.append(self.name)
    print(f"The {self.name} finished")