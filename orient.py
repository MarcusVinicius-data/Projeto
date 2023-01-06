class People:
    def __init__(self, name, last_name) -> None:
        self.name = name
        self.last_name = last_name
        
        
p1 = People('Marcus', 'Vinicius')
print(p1.name, p1.last_name)

p2 = People('Salete', 'Eliana')
print(p2.name, p2.last_name)       