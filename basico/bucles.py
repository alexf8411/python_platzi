# contador = 0
# print(f"2 elevado a {contador} es igual a: {(2 ** contador)}")

def run ():
    LIMITE = 1000000 #Es una contante por ir en mayusculas

    contador = 0
    potencia_2 = 2 ** contador
    while potencia_2 < LIMITE:
       print(f"2 elevado a {contador} es igual a: {potencia_2}") 
       contador += 1
       potencia_2 = 2 ** contador


    pass
if __name__ == '__main__':
    run()