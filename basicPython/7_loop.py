# Buzz Fizz
# 1. imprimir los numeros del 1 al 100
# 2. para los multiplos de 3 en vez de imprimir el numero, imprima fizz.
# 3. para los multiplos de 5 en lugar de imprimir el numero, imprima buzz.
# 4. para los numeros multiplos de 3 y 5, imprima buzz fizz.

for numbers in range(1, 101):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print('buzz fizz')
    elif numbers % 3 == 0:
        print('fizz')
    elif numbers % 5 == 0:
        print('buzz')
    else:
        print(numbers)
