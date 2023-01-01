class Car:
    def __init__(self, name):
        self.name = name

    def acelerar(self):
        print(f'{self.name} está acelerando')


vehicle = Car(name='Fusca')
print(vehicle.name)
vehicle.acelerar()

vehicle2 = Car(name='Celta')
print(vehicle2.name)
vehicle2.acelerar()



