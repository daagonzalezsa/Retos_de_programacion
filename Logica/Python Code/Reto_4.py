# Logica: Reto 4
# Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.

Primes = []
for i in range(1, 101):
    divisors = []
    for j in range(1,i+1):
        if (i % j==0):
            divisors.append(j)
    if len(divisors) <= 2:
        Primes.append(i)

print(Primes)
