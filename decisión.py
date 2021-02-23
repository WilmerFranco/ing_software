# Imprimimos el menú en pantalla
print("""Seleccione una de las siguientes opciones
    1) Nivelación       2) Poligonal
    """)
# Leemos lo que ingresa el usuario
eligio=input("-que deseas calcular :")

# Según lo que ingresó, código diferenteif eligio=="1":
    #print ("Listamos otras herramientas")
if  eligio == "1":
    print("Eligio Nivelación")
    print("""Seleccione uno de los siguientes ajustes
    1) Calculo por distancias       2) Calculo por pesos
    """)
    CalNiv=input("¿por cual método desea calcular?")
    if CalNiv == "1":
        print("Eligio calculo por distancias")
    elif CalNiv == "2":
        print("Eligio calculo por pesos")
    else:
        print("Opción no válida")
elif eligio == "2":
    print("Eligio poligonal")
    print("""Indique si la poligonal es Abierta o cerrada
    1) Abierta       2) Cerrada
    """)
    poligonal=input()
    if poligonal == "1":
        print("Eligio poligonal abierta")
        print("""Indique por cual método desea calcular
    1) Crandall     2) Brújula      3) Tránsito
    """)
        poligonal=input()
        if poligonal == "1":
            print("Eligio ajuste por método Crandall")
        elif poligonal == "2":
            print("Eligio ajuste por método Brujula")
        elif poligonal == "3":
            print("Eligio ajuste por método Tránsito")
        else:
            print("Opción no válida")
    elif poligonal == "2":
        print("Eligio poligonal cerrada")
        print("""Indique por cual método desea calcular
    1) Crandall     2) Brújula      3) Tránsito
    """)
        poligonal=input()
        if poligonal == "1":
            print("Eligio ajuste por método Crandall")
        elif poligonal == "2":
            print("Eligio ajuste por método Brujula")
        elif poligonal == "3":
            print("Eligio ajuste por método Tránsito")
        else:
            print("Opción no válida")
    else:
        print("Opción no válida")

else:
    print("Opción no válida")