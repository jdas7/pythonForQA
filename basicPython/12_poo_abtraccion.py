from abc import ABC, abstractmethod


class Employees(ABC):
    def __init__(self, nombre, salario):
        self.name = nombre
        self.salary = salario

    @abstractmethod
    def calculate_salary(self):
        pass


class Developer(Employees):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.language = lenguaje

    def calculate_salary(self):
        return self.salary * 1.2


class Product(Employees):
    def __init__(self, nombre, salario, nivel):
        super().__init__(nombre, salario)
        self.level = nivel

    def calculate_salary(self):
        return self.salary * 1.5


# instanciar clases y metodos
developer_david = Developer(nombre="David", salario=10000000, lenguaje="Python")
product_juan = Product(nombre="juan", salario=12000000, nivel="alto")

# calculo de sueldos
salary_developer = developer_david.calculate_salary()
salary_product = product_juan.calculate_salary()

print(f"el sueldo de {developer_david.name}: {salary_developer}")
print(f"el sueldo de {product_juan.name}: {salary_product}")

