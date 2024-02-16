# Python is dynamically typed

# Data type is integer or long
data_integer = 15
print(type(data_integer))

# Data type is float
data_float = 1.0
print(type(data_float))

# Complex data type
data_complex = 1 + 1j
print(type(data_complex), data_complex)

# Data type is String
data_string = "HOLA"
print(type(data_string))

# Data type is booleano
data_booleano = True
print(type(data_booleano))

booleano = 5 == 4
print(type(booleano), booleano)

#  Data type is None
data_none = None
print(type(data_none))

# Data type is list
data_list = []
print(type(data_list))

# Data type is tuple
data_tuple = ("juan", "Perez", 25)
print(type(data_tuple), data_tuple)

# Data type is dictionary
data_dictionary = {
    "a": 1,
    "b": 2
}
print(type(data_dictionary), data_dictionary)

# Direction of memory in RAM
print(id(data_dictionary))

# concatenation
print(data_string + ", " + "My age is:", data_integer, "fin: " + str(data_integer))

num1 = "5"
num2 = "4"

print("concatenation: ", num1 + num2)
print("suma with transformation: ", int(num1) + int(num2))
