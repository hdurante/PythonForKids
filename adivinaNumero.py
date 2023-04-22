import random

print("Adivina el numero que estoy pensando entre 1 y 1000")
numero = int(input('Dime un numero: '))
numeroAlAzar = random.randint(1, 1000)

while(True):
    if numero > numeroAlAzar:
        numero = int(input('Fallaste, el numero es menor dime otro numero : '))
    elif numero < numeroAlAzar:
        numero = int(input('Fallaste, el numero es MAYOR dime otro numero: '))
    elif numero == numeroAlAzar:
        print('Felicidades hacker ganaste')
        break

    
