from random import randint
from time import sleep
from threading import Thread
from tqdm import tqdm

class Car(Thread):
    """Uma classe Car que estende Thread, simulando uma corrida de carros onde cada carro corre em sua própria thread.
    
    Atributos:
        winners (dict): Uma variável de classe que armazena os vencedores da corrida em ordem.
        position (int): Uma variável de classe que rastreia a posição de chegada dos carros.
    """
    
    winners = {}
    position = 0

    def __init__(self, name, speed, color):
        """Inicializa um novo objeto Car.
        
        Args:
            name (str): O nome do carro.
            speed (int): A velocidade com que o carro se move (distância por unidade de tempo).
            color (str): A cor da barra de progresso no console.
        """
        super().__init__()
        self.name = name
        self.speed = speed
        self.color = color
        self.displacement = 0

    def run(self):
        """Simula a corrida do carro.
        
        Usa uma barra de progresso para exibir visualmente a corrida no console. O progresso do carro é atualizado
        com base em sua velocidade. Aleatoriamente, o carro pode 'dormir' por 6 segundos para simular um atraso. Uma vez que o carro
        termina a corrida, seu nome e posição são registrados na variável de classe 'winners'.
        """
        with tqdm(total=100, desc=self.name, colour=self.color, leave=False, 
                  bar_format='{desc:<20}: {bar} {n_fmt}/{total_fmt}', ncols=100) as progress_bar:
            while self.displacement < 100:
                self.displacement += self.speed
                progress_bar.update(self.speed)

                # Simula aleatoriamente um atraso na corrida
                if randint(1, 10) == 7:
                    sleep(6)

                sleep(2)  # Simula a passagem do tempo entre os movimentos

            Car.position += 1
            Car.winners[self.name] = Car.position
