class Car:
    def __init__(self, name) -> None:
        self.name = name
        self._motor = None
        self._manufacturer = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, value) -> None:
        self._motor = value

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value


class Motor:
    def __init__(self, name) -> None:
        self.name = name


class Manufacturer:
    def __init__(self, name) -> None:
        self.name = name


vehicle1 = Car('JETTA')
team1 = Manufacturer('volkswagen')
motorType = Motor('2.0')
vehicle1.manufacturer = team1
vehicle1.motor = motorType
print(vehicle1.name, vehicle1.manufacturer.name, vehicle1.motor.name)
print('-------------------------------------------------------------------')
vehicle2 = Car('Carrera GT')
team2 = Manufacturer('PORSHE')
motorType2 = Motor('4.0')
vehicle2.manufacturer = team2
vehicle2.motor = motorType2
print(vehicle2.name, vehicle2.manufacturer.name, vehicle2.motor.name)
