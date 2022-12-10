from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def PickingThePassenger(self) -> None: pass


class LuxuryCar(Vehicle):
    def PickingThePassenger(self) -> None:
        print('carro de luxo buscando cliente')


"""pode ser feito com mais classes no caso abaixo classe PopularCar de exemplo """


class PopularCar(Vehicle):
    def PickingThePassenger(self) -> None:
        print('carro popular buscando cliente')
        

class Motorcycle(Vehicle):
    def PickingThePassenger(self) -> None:
        print('Moto popular buscando cliente')        


"""criação de uma simple factory como no exemplo ;  
A criação de um sistema de aplicativo de viagem uber, 99 taxi e etc"""


class FactoryVehicle:  # dentro dessa factory vai ser criado os produtos das classes acima
    @staticmethod  # a classe 'FactoryVehicle' vai retornar  um veiculo aleatoriamente
    def getCar(tipo: str) -> Vehicle:
        # emplementa esse metodo criando condição nesse caso carro de luxo e carro popular
        if tipo == 'Luxo':
            return LuxuryCar()
        if tipo == 'Popular':
            return PopularCar()
        assert 0, 'Veiculo não existe'  # assert error carro o sistema não busque nenhum do dois tipos de veiculos


if __name__ == "__main__":
    from random import choice

    carsAvailable = ['Luxo', 'Popular', 'Moto']

    for i in range(10):
        car = FactoryVehicle.getCar(choice(carsAvailable))
        car.PickingThePassenger()
