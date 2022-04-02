def run():
    mi_diccionario = {
        "llave1" : 1,
        "llave2" : 2,
        "llave3" : 3

    }
    print(mi_diccionario["llave2"])

    poblacion_paises = {
        "Argentina" : 45000000,
        "Brasil" : 210000000,
        "Colombia" : 50000000
    }

    print(poblacion_paises["Argentina"])

    for pais in poblacion_paises.keys():
        print(pais)

    for pais in poblacion_paises.values():
        print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(pais+ " Tiene " + str(poblacion)+" habitantes")

if __name__ == '__main__':
    run()