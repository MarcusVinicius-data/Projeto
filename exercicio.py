class People:
    CurrentYear = 2023

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def YearOfBirth(self):
        return People.CurrentYear - self.age


data = {'name': 'Marcus Vinicius', 'age': 28}
people1 = People(**data)


"""print(people1.__dict__)
print(people2.__dict__)
print(people3.__dict__)]
"""
# people = People(**data)
print(vars(people1))
print(people1.name)
# print(vars(people2))
# print(vars(people3))
