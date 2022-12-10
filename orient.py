class  People:
    def __init__(self, name, last_name) -> None:
        self.name = name
        self.last_name = last_name
    
p1 =  People('Marcus', 'Vinicius')

#p1.name = 'Marcus'
#p1.last_name = 'Vincius'  

p2 = People('Salete', 'Eliana')

#p2.name = 'Salete'
#p2.last_name = 'Eliana'
    
print(p1.name)
print(p1.last_name)
print(p2.name)
print(p2.last_name)