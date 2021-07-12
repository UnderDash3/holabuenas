import matplotlib.pyplot as plt

regiones=["Arica y Parinacota", "Tarapacá", "Antofagasta", "Atacama", "Coquimbo", "Valparaíso", "Metropolitana", "O’Higgins", "Maule", "Ñuble", "Biobío", "Araucanía", "Los Ríos", "Los Lagos", "Aysén", "Magallanes"]
print(regiones)

##validaciones de regiones 

opcionRegiones=input("[a] Ingrese nombre de region: ")
while opcionRegiones not in regiones: 
  opcionRegiones=input("Error ingrese una region valida: ")

##Datos de las regiones sin sintomaS junto a su respectivo grafico

if opcionRegiones == "Tarapacá":
    print("Region De Tarapacá")
    opcionUsuario = "6"
    while opcionUsuario != "3":
        print("----------------------------------")
        print("(1)Mostrar contagiados sin sintomas")
        print("(2)Mostrar contagiados Con Sintomas")
        print("(3)Salir")
        opcionUsuario = input("Ingrese una opcion: ")
        while opcionUsuario not in ["1","2","3"]:
            print("Opcion incorrecta")
            break
        if opcionUsuario == "1":
            print("Contagiados sin sintomas")
            dias = ["1", "2", "3" , "4", "5", "6", "7" , "8" , "9" , "10" , "11" , "12" ,"13" , "14" ] 
            casos = [ 21,13,16,20,2,4,14,15,11,13,6,3,24,13 ] 
            colors = ["blue", "blue" , "blue" , "blue" , "blue" , "blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,] 
            plt.title("Casos Sin Sintomas")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
        elif opcionUsuario =="2":
            print("Contagiados con sintomas")
        else:
            print("Ingrese número correcto")

if opcionRegiones == "Arica y Parinacota":
    print("Region De Arica y Parinacota")
    opcionUsuario = "6"
    while opcionUsuario != "3":
        print("----------------------------------")
        print("(1)Mostrar contagiados sin sintomas")
        print("(2)Mostrar contagiados Con Sintomas")
        print("(3)Salir")
        opcionUsuario = input("Ingrese una opcion: ")
        while opcionUsuario not in ["1","2","3"]:
            print("Opcion incorrecta")
            break
        if opcionUsuario == "1":
            print("Contagiados sin sintomas")
            dias = ["1", "2", "3" , "4", "5", "6", "7" , "8" , "9" , "10" , "11" , "12" ,"13" , "14" ] 
            casos = [37,30,41,10,8,15,32,29,24,24,14,5,27,31 ] 
            colors = ["blue", "blue" , "blue" , "blue" , "blue" , "blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,] 
            plt.title("Casos Sin Sintomas")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
        elif opcionUsuario =="2":
            print("Contagiados con sintomas")
        else:
            print("Ingrese número correcto")

if opcionRegiones == "Antofagasta":
    print("Region De Antofagasta")
    opcionUsuario = "6"
    while opcionUsuario != "3":
        print("----------------------------------")
        print("(1)Mostrar contagiados sin sintomas")
        print("(2)Mostrar contagiados Con Sintomas")
        print("(3)Salir")
        opcionUsuario = input("Ingrese una opcion: ")
        while opcionUsuario not in ["1","2","3"]:
            print("Opcion incorrecta")
            break
        if opcionUsuario == "1":
            print("Contagiados sin sintomas")
            dias = ["1", "2", "3" , "4", "5", "6", "7" , "8" , "9" , "10" , "11" , "12" ,"13" , "14" ] 
            casos = [59,35,119,21,7,26,52,64,34,28,7,10,54,31] 
            colors = ["red", "blue" , "green" , "black" , "blue" , "blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,] 
            plt.title("Casos Sin Sintomas")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
        elif opcionUsuario =="2":
            print("Contagiados con sintomas")
        else:
            print("Ingrese número correcto")

if opcionRegiones == "Atacama":
    print("Region De Atacama")
    opcionUsuario = "6"
    while opcionUsuario != "3":
        print("----------------------------------")
        print("(1)Mostrar contagiados sin sintomas")
        print("(2)Mostrar contagiados Con Sintomas")
        print("(3)Salir")
        opcionUsuario = input("Ingrese una opcion: ")
        while opcionUsuario not in ["1","2","3"]:
            print("Opcion incorrecta")
            break
        if opcionUsuario == "1":
            print("Contagiados sin sintomas")
            dias = ["1", "2", "3" , "4", "5", "6", "7" , "8" , "9" , "10" , "11" , "12" ,"13" , "14" ] 
            casos = [51,34,12,64,51,58,42,71,6,38,33,25,53,87 ] 
            colors = ["red", "blue" , "green" , "black" , "blue" , "blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,] 
            plt.title("Casos Sin Sintomas")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
        elif opcionUsuario =="2":
            print("Contagiados con sintomas")
        else:
            print("Ingrese número correcto")
 
if opcionRegiones == "Coquimbo":
    print("Region De Coquimbo")
    opcionUsuario = "6"
    while opcionUsuario != "3":
        print("----------------------------------")
        print("(1)Mostrar contagiados sin sintomas")
        print("(2)Mostrar contagiados Con Sintomas")
        print("(3)Salir")
        opcionUsuario = input("Ingrese una opcion: ")
        while opcionUsuario not in ["1","2","3"]:
            print("Opcion incorrecta")
            break
        if opcionUsuario == "1":
            print("Contagiados sin sintomas")
            dias = ["1", "2", "3" , "4", "5", "6", "7" , "8" , "9" , "10" , "11" , "12" ,"13" , "14" ] 
            casos = [48,47,42,29,17,23,25,58,40,33,36,12,33,43 ] 
            colors = ["red", "blue" , "green" , "black" , "blue" , "blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,] 
            plt.title("Casos Sin Sintomas")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
        elif opcionUsuario =="2":
            print("Contagiados con sintomas")
        else:
            print("Ingrese número correcto")

if opcionRegiones == "Valparaíso":
    print("Region De Valparaíso")
    opcionUsuario = "6"
    while opcionUsuario != "3":
        print("----------------------------------")
        print("(1)Mostrar contagiados sin sintomas")
        print("(2)Mostrar contagiados Con Sintomas")
        print("(3)Salir")
        opcionUsuario = input("Ingrese una opcion: ")
        while opcionUsuario not in ["1","2","3"]:
            print("Opcion incorrecta")
            break
        if opcionUsuario == "1":
            print("Contagiados sin sintomas")
            dias = ["1", "2", "3" , "4", "5", "6", "7" , "8" , "9" , "10" , "11" , "12" ,"13" , "14" ] 
            casos = [116,95,90,31,27,29,68,95,62,61,37,28,57,67] 
            colors = ["red", "blue" , "green" , "black" , "blue" , "blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,] 
            plt.title("Casos Sin Sintomas")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
        elif opcionUsuario =="2":
            print("Contagiados con sintomas")
        else:
            print("Ingrese número correcto")

if opcionRegiones == "Metropolitana":
    print("Region De Metropolitana")
    opcionUsuario = "6"
    while opcionUsuario != "3":
        print("----------------------------------")
        print("(1)Mostrar contagiados sin sintomas")
        print("(2)Mostrar contagiados Con Sintomas")
        print("(3)Salir")
        opcionUsuario = input("Ingrese una opcion: ")
        while opcionUsuario not in ["1","2","3"]:
            print("Opcion incorrecta")
            break
        if opcionUsuario == "1":
            print("Contagiados sin sintomas")
            dias = ["1", "2", "3" , "4", "5", "6", "7" , "8" , "9" , "10" , "11" , "12" ,"13" , "14" ] 
            casos = [447,415,364,161,98,157,286,272,289,250,133,161,222,260 ] 
            colors = ["red", "blue" , "green" , "black" , "blue" , "blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,] 
            plt.title("Casos Sin Sintomas")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
        elif opcionUsuario =="2":
            print("Contagiados con sintomas")
        else:
            print("Ingrese número correcto")

if opcionRegiones == "O’Higgins":
    print("Region De O’Higgins")
    opcionUsuario = "6"
    while opcionUsuario != "3":
        print("----------------------------------")
        print("(1)Mostrar contagiados sin sintomas")
        print("(2)Mostrar contagiados Con Sintomas")
        print("(3)Salir")
        opcionUsuario = input("Ingrese una opcion: ")
        while opcionUsuario not in ["1","2","3"]:
            print("Opcion incorrecta")
            break
        if opcionUsuario == "1":
            print("Contagiados sin sintomas")
            dias = ["1", "2", "3" , "4", "5", "6", "7" , "8" , "9" , "10" , "11" , "12" ,"13" , "14" ] 
            casos = [47,51,40,17,14,15,36,51,38,30,8,14,28,38 ] 
            colors = ["red", "blue" , "green" , "black" , "blue" , "blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,] 
            plt.title("Casos Sin Sintomas")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
        elif opcionUsuario =="2":
            print("Contagiados con sintomas")
        else:
            print("Ingrese número correcto")

if opcionRegiones == "Maule":
    print("Region De Maule")
    opcionUsuario = "6"
    while opcionUsuario != "3":
        print("----------------------------------")
        print("(1)Mostrar contagiados sin sintomas")
        print("(2)Mostrar contagiados Con Sintomas")
        print("(3)Salir")
        opcionUsuario = input("Ingrese una opcion: ")
        while opcionUsuario not in ["1","2","3"]:
            print("Opcion incorrecta")
            break
        if opcionUsuario == "1":
            print("Contagiados sin sintomas")
            dias = ["1", "2", "3" , "4", "5", "6", "7" , "8" , "9" , "10" , "11" , "12" ,"13" , "14" ] 
            casos = [84,102,100,58,30,44,83,64,76,56,20,6,68,32 ] 
            colors = ["red", "blue" , "green" , "black" , "blue" , "blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,] 
            plt.title("Casos Sin Sintomas")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
        elif opcionUsuario =="2":
            print("Contagiados con sintomas")
        else:
            print("Ingrese número correcto")

if opcionRegiones == "Ñuble":
    print("Region De Ñuble")
    opcionUsuario = "6"
    while opcionUsuario != "3":
        print("----------------------------------")
        print("(1)Mostrar contagiados sin sintomas")
        print("(2)Mostrar contagiados Con Sintomas")
        print("(3)Salir")
        opcionUsuario = input("Ingrese una opcion: ")
        while opcionUsuario not in ["1","2","3"]:
            print("Opcion incorrecta")
            break
        if opcionUsuario == "1":
            print("Contagiados sin sintomas")
            dias = ["1", "2", "3" , "4", "5", "6", "7" , "8" , "9" , "10" , "11" , "12" ,"13" , "14" ] 
            casos = [15,12,13,10,6,3,16,11,17,16,8,9,18,17] 
            colors = ["red", "blue" , "green" , "black" , "blue" , "blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,] 
            plt.title("Casos Sin Sintomas")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
        elif opcionUsuario =="2":
            print("Contagiados con sintomas")
        else:
            print("Ingrese número correcto")

if opcionRegiones == "Biobío":
    print("Region De Biobío")
    opcionUsuario = "6"
    while opcionUsuario != "3":
        print("----------------------------------")
        print("(1)Mostrar contagiados sin sintomas")
        print("(2)Mostrar contagiados Con Sintomas")
        print("(3)Salir")
        opcionUsuario = input("Ingrese una opcion: ")
        while opcionUsuario not in ["1","2","3"]:
            print("Opcion incorrecta")
            break
        if opcionUsuario == "1":
            print("Contagiados sin sintomas")
            dias = ["1", "2", "3" , "4", "5", "6", "7" , "8" , "9" , "10" , "11" , "12" ,"13" , "14" ] 
            casos = [87,83,82,24,15,39,90,57,76,71,27,16,74,59] 
            colors = ["red", "blue" , "green" , "black" , "blue" , "blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,] 
            plt.title("Casos Sin Sintomas")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
        elif opcionUsuario =="2":
            print("Contagiados con sintomas")
        else:
            print("Ingrese número correcto")

if opcionRegiones == "Araucanía":
    print("Region De Araucanía")
    opcionUsuario = "6"
    while opcionUsuario != "3":
        print("----------------------------------")
        print("(1)Mostrar contagiados sin sintomas")
        print("(2)Mostrar contagiados Con Sintomas")
        print("(3)Salir")
        opcionUsuario = input("Ingrese una opcion: ")
        while opcionUsuario not in ["1","2","3"]:
            print("Opcion incorrecta")
            break
        if opcionUsuario == "1":
            print("Contagiados sin sintomas")
            dias = ["1", "2", "3" , "4", "5", "6", "7" , "8" , "9" , "10" , "11" , "12" ,"13" , "14" ] 
            casos = [115,104,115,32,25,22,83,83,70,67,32,21,42,52 ] 
            colors = ["red", "blue" , "green" , "black" , "blue" , "blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,] 
            plt.title("Casos Sin Sintomas")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
        elif opcionUsuario =="2":
            print("Contagiados con sintomas")
        else:
            print("Ingrese número correcto")

if opcionRegiones == "Los Ríos":
    print("Region De Los Ríos")
    opcionUsuario = "6"
    while opcionUsuario != "3":
        print("----------------------------------")
        print("(1)Mostrar contagiados sin sintomas")
        print("(2)Mostrar contagiados Con Sintomas")
        print("(3)Salir")
        opcionUsuario = input("Ingrese una opcion: ")
        while opcionUsuario not in ["1","2","3"]:
            print("Opcion incorrecta")
            break
        if opcionUsuario == "1":
            print("Contagiados sin sintomas")
            dias = ["1", "2", "3" , "4", "5", "6", "7" , "8" , "9" , "10" , "11" , "12" ,"13" , "14" ] 
            casos = [99,110,65,50,27,40,109,98,111,62,34,22,79,60 ] 
            colors = ["red", "blue" , "green" , "black" , "blue" , "blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,] 
            plt.title("Casos Sin Sintomas")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
        elif opcionUsuario =="2":
            print("Contagiados con sintomas")
        else:
            print("Ingrese número correcto")

if opcionRegiones == "Los Lagos":
    print("Region De Los Lagos")
    opcionUsuario = "6"
    while opcionUsuario != "3":
        print("----------------------------------")
        print("(1)Mostrar contagiados sin sintomas")
        print("(2)Mostrar contagiados Con Sintomas")
        print("(3)Salir")
        opcionUsuario = input("Ingrese una opcion: ")
        while opcionUsuario not in ["1","2","3"]:
            print("Opcion incorrecta")
            break
        if opcionUsuario == "1":
            print("Contagiados sin sintomas")
            dias = ["1", "2", "3" , "4", "5", "6", "7" , "8" , "9" , "10" , "11" , "12" ,"13" , "14" ] 
            casos = [83,63,72,43,18,6,57,52,42,53,55,14,52,35 ] 
            colors = ["red", "blue" , "green" , "black" , "blue" , "blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,] 
            plt.title("Casos Sin Sintomas")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
        elif opcionUsuario =="2":
            print("Contagiados con sintomas")
        else:
            print("Ingrese número correcto")

if opcionRegiones == "Aysén":
    print("Region De Aysén")
    opcionUsuario = "6"
    while opcionUsuario != "3":
        print("----------------------------------")
        print("(1)Mostrar contagiados sin sintomas")
        print("(2)Mostrar contagiados Con Sintomas")
        print("(3)Salir")
        opcionUsuario = input("Ingrese una opcion: ")
        while opcionUsuario not in ["1","2","3"]:
            print("Opcion incorrecta")
            break
        if opcionUsuario == "1":
            print("Contagiados sin sintomas")
            dias = ["1", "2", "3" , "4", "5", "6", "7" , "8" , "9" , "10" , "11" , "12" ,"13" , "14" ] 
            casos = [19,31,16,5,3,11,13,8,19,8,2,12,22,4 ] 
            colors = ["red", "blue" , "green" , "black" , "blue" , "blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,] 
            plt.title("Casos Sin Sintomas")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
        elif opcionUsuario =="2":
            print("Contagiados con sintomas")
        else:
            print("Ingrese número correcto")

if opcionRegiones == "Magallanes":
    print("Region De Magallanes")
    opcionUsuario = "6"
    while opcionUsuario != "3":
        print("----------------------------------")
        print("(1)Mostrar contagiados sin sintomas")
        print("(2)Mostrar contagiados Con Sintomas")
        print("(3)Salir")
        opcionUsuario = input("Ingrese una opcion: ")
        while opcionUsuario not in ["1","2","3"]:
            print("Opcion incorrecta")
            break
        if opcionUsuario == "1":
            print("Contagiados sin sintomas")
            dias = ["1", "2", "3" , "4", "5", "6", "7" , "8" , "9" , "10" , "11" , "12" ,"13" , "14" ] 
            casos = [6,3,5,4,6,1,11,2,2,1,3,1,0,3 ] 
            colors = ["red", "blue" , "green" , "black" , "blue" , "blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,] 
            plt.title("Casos Sin Sintomas")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
        elif opcionUsuario =="2":
            print("Contagiados con sintomas")
        else:
            print("Ingrese número correcto")

##menu
opcionUsuario = "6"
while opcionUsuario != "3":
  print("----------------------------------")
  print("(1)Mostrar contagiados sin sintomas")
  print("(2)Mostrar contagiados Con Sintomas")
  print("(3)Salir")
  opcionUsuario = input("Ingrese una opcion: ")
  while opcionUsuario not in ["1","2","3"]:
    print("Opcion incorrecta")
    opcionUsuario = input("Ingrese una opcion: ")
  if opcionUsuario == "1":
    print("Contagiados sin sintomas")
  elif opcionUsuario =="2":
    print("Contagiados con sintomas")