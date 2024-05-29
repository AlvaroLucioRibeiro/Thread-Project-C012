from random import randint
from time import sleep
from threading import Thread, Semaphore, Lock
from tqdm import tqdm

class Car(Thread):
    """Uma classe Car que estende Thread, simulando uma corrida de carros onde cada carro corre em sua própria thread.
    
    Atributos:
        winners (dict): Uma variável de classe que armazena os vencedores da corrida em ordem.
        position (int): Uma variável de classe que rastreia a posição de chegada dos carros.
    """
    
    winners = {}
    countID = 0
    position = 0
    power_used = False  # Flag para verificar se o poder já foi usado
    semaphore = Semaphore(1)  # Semáforo para garantir exclusão mútua
    lock = Lock()  # Lock para garantir que a posição e os vencedores sejam atualizados de forma atômica

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
        self.id = Car.countID
        Car.countID += 1

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

                # Usar semáforo para garantir que apenas um carro receba o poder
                with Car.semaphore:
                    if not Car.power_used and randint(1, 20) == 10:
                        self.speed *= 2
                        Car.power_used = True
                        tqdm.write(f"{self.name} pegou o poder e teve a velocidade dobrada!")

                sleep(2)  # Simula a passagem do tempo entre os movimentos

            with Car.lock:
                if self.name not in Car.winners:
                    Car.position += 1
                    Car.winners[self.name] = Car.position
