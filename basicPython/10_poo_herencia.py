class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass


# herencia
class Dog(Animal):
    def sound(self):
        print("bark!!")


class Cat(Animal):
    def sound(self):
        print("miau!!")


perro = Dog("Sanson")
gato = Cat("sr. galleta")

perro.sound()  # bark!!
gato.sound()  # miau!!
