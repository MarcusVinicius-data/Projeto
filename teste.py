class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def createWith_50_years(cls, name):
        return cls(name, 50)
    
    @classmethod
    def no_name(cls, age):
        return cls("No name", age)   
        
        
people1 = People('Marcus', 28)
people2 = People.createWith_50_years('Joana')
people3 = People.no_name(38)
print(people1.name, people2.name, people3.name)
print(people1.age, people2.age, people3.age)
        