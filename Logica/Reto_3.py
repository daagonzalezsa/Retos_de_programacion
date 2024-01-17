# Logica: Reto 3
# Escribe un programa que imprima los 50 primeros números de la sucesión
# de Fibonacci empezando en 0.
# - La serie Fibonacci se compone por una sucesión de números en
# la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13...

import sys

def Fibonacci(n = 50):
    numbers = [0, 1]
    for i in range(n+1):
        if i > 1:
            numbers.append(numbers[i-1] + numbers[i-2])

    print(numbers)

if __name__ == '__main__':
    Fibonacci(int(sys.argv[1]))