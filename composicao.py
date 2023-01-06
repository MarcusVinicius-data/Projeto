class Client:
    def __init__(self, name) -> None:
        self.name = name
        self.andress = []

    def enter_andress(self, street, number):
        self.andress.append(Andress(street, number))

    def inset_external_andress(self, andress):
        self.andress.append(andress)

    def list_addresses(self):
        for andress in self.andress:
            print(andress.street, andress.number)

    def __del__(self):
        print('DELETING,', self.name)


class Andress:
    def __init__(self, street, number) -> None:
        self.street = street
        self.number = number

    def __del__(self):
        print('DELETING,', self.street, self.number)


client1 = Client('Marcus')
client1.enter_andress('Pedro Charuto', 63)
client1.enter_andress('Joaquim Barreto', 105)
external_andress = Andress('Avenida Men de Sá', 685)
client1.inset_external_andress(external_andress)
client1.list_addresses()

del client1
print(external_andress.street, external_andress.number)
print('-------------------------------------------------')
