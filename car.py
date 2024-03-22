from random import randint
from time import sleep
from threading import Thread
from tqdm import tqdm

class Car(Thread):
  winners = {}
  position = 0

  def __init__(self, name, speed, color):
    super().__init__()
    self.name = name
    self.speed = speed
    self.color = color
    self.displacement = 0

  def run(self):
    with tqdm(total=100, desc=self.name, colour=self.color, leave=False, bar_format='{desc:<20}: {bar} {n_fmt}/{total_fmt}', ncols=100) as progress_bar:
        while self.displacement < 100:
            self.displacement += self.speed
            progress_bar.update(self.speed)

            if randint(1, 10) == 7:
                sleep(6)

            sleep(2)

        Car.position += 1
        Car.winners[self.name] = Car.position
        