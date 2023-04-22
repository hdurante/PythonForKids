import random

opciones = ["piedra", "papel", "tijeras"]

while(True):
    print('***************Listo para jugar***************')
    print('0 - Piedra')
    print('1 - Papel')
    print('2 - Tijeras') 

    Elegiste = int(input('Elige la opcion: '))
    computadoraElije= random.choice(opciones)
    
    if opciones[Elegiste] == computadoraElije:    
        print(f"Elegi {computadoraElije} Empatamos")
    elif opciones[Elegiste] == 'piedra' and computadoraElije == 'tijeras':    
        print(f"Elegi {computadoraElije} Felicidades me ganaste :)")
    elif  opciones[Elegiste] == 'papel' and computadoraElije == 'piedra':    
        print(f"Elegi {computadoraElije} Felicidades me ganaste :)")
    elif  opciones[Elegiste] == 'tijeras' and computadoraElije == 'papel':    
        print(f"Elegi {computadoraElije} Felicidades me ganaste :)")
    elif opciones[Elegiste] == 'tijeras' and computadoraElije == 'piedra':    
        print(f"Elegi {computadoraElije} yo gane")
    elif  opciones[Elegiste] == 'piedra' and computadoraElije == 'papel':    
        print(f"Elegi {computadoraElije} yo gane")
    elif  opciones[Elegiste] == 'papel' and computadoraElije == 'tijeras':    
        print(f"Elegi {computadoraElije} yo gane")    



