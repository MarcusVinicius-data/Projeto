# class Car:
#    def __init__(self, name) -> None:
#        self.name = name
        
#    def SpeedUp(self):
#        print(f'{self.name} está acelerando...')
        
#fusca = Car('Fusca')
#print(fusca.name)
#fusca.SpeedUp()  

#celta = Car('Celta')
#print(celta.name)
#celta.SpeedUp() 

class Camera:
    def __init__(self, name, shooting=False) -> None:
        self.name = name
        self.shooting = shooting
        
    def Film(self) -> None:
        print(f'{self.name} já está filmando...') # imprime na tela oque a camera está faznedo
        return # return para parar a ação  
    
        print(f'{self.name} , está filmando')
        shooting = True 
    
       # execução de parada
       
    def StopFilming(self):
        if not self.shooting:
            print(f'{self.name} NÃO está filmando...')
            return

        print(f'{self.name} está parando de filmar...')
        self.shooting = False

    def Photograph(self):
        if self.shooting:
            print(f'{self.name} não pode fotografar filmando')
            return

        print(f'{self.name} está fotografando...')
    
 
 
    
cam1 = Camera('Canon')
cam2 = Camera('kodak')
cam3 = Camera('Sony')             
  
cam1.Film()
cam1.StopFilming()
cam1.Photograph()
cam1.Photograph()

print()

cam2.Film()
cam2.StopFilming()
cam2.Photograph()
cam2.Film()

print()

cam3.Film()
cam3.StopFilming()
cam3.Photograph() 
