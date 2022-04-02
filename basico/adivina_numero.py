import random


def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input("Elige un número del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            numero_elegido = int(input("Busca un número mas grande: "))
        else:
            numero_elegido = int(input("Busca un número mas pequeño: "))
    print ("Ganaste!")


if __name__ == '__main__':
    run()