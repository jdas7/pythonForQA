class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def say_name(self):
        print(f'your name is: {self.name}')
        print(f'your age is: {self.age}')


person1 = Person("David", 30)
person2 = Person("Juan", 27)

print(person1.name)
person2.say_name()
