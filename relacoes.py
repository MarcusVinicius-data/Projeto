'''class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('Marcus')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina')
escritor.ferramenta = maquina_de_escrever

print(caneta.escrever())
print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())'''


class Vehicle:
    def __init__(self, name):
        self.name = name
        self._genre = None
    
        
    @property
    def genre(self, genre):
        self._genre = genre  
     
        
class StyleVehicle:
    def __init__(self, style):
        self.style = style
        
    def driving(self):
        return f'{self.style} is running'
    

vehicle = Vehicle('Mini Cooper')
style = StyleVehicle('Cooper S')
pilot_driving = StyleVehicle('Marcus Vinicius')
Vehicle.genre = pilot_driving
print()
print(style.driving())
print(pilot_driving.driving())
print(vehicle.genre.driving())