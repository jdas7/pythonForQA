class Car:
    def __init__(self, marca, modelo):  # Definir funcion
        self.marca = marca
        self.modelo = modelo

    def mostar_info(self):
        print(f'Mi coche: {self.marca} {self.modelo}')


# instaciar objetos
car1 = Car("Toyota", "Corolla")

# Acceder a los atributos y llamar el metodo
print(car1.marca)
car1.mostar_info()
