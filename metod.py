class Camera:
    def __init__(self, name, filming=False) -> None:
        self.name = name
        self.filming = filming
        
    def Filming(self):
        if self.filming:
            print(f'{self.name} start filming')
            return
        print(f'{self.name} keep filming')
        self.filming = True
        
    def StopFilming(self):
        if not self.filming:
            print(f'{self.name} stopping filming') 
            return
        
        print(f'{self.name} stopped filming')
        self.filming = False
        
    def StartPhotographic(self):
        if self.filming:
            print(f"{self.name} can't shoot, it's taking a picture, please switch to photo mode")
            return
        print(f'{self.name} is photographing')       
            

cam1 = Camera('Sony')
cam2 = Camera('Tecpix')
cam3 = Camera('Cannon 800')

cam1.StartPhotographic()
cam2.Filming()
cam3.StartPhotographic()
cam2.StartPhotographic()
cam1.Filming()
cam3.Filming()
cam2.StopFilming()
cam2.StartPhotographic()
print()
cam2.StopFilming()
cam2.StartPhotographic()