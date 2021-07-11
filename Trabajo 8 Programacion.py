
import matplotlib.pyplot as plt

##lista de las regiones

regiones=["Arica y Parinacota", "Tarapacá", "Antofagasta", "Atacama", "Coquimbo", "Valparaíso", "Metropolitana", "O’Higgins", "Maule", "Ñuble", "Biobío", "Araucanía", "Los Ríos", "Los Lagos", "Aysén", "Magallanes"]
print(regiones)

##validaciones de regiones 

opcionRegiones=input("[a] Ingrese nombre de region: ")
while opcionRegiones not in regiones: 
  opcionRegiones=input("Error ingrese una region valida: ")


if opcionRegiones =="Tarapacá":
  print("Region De Tarapacá")
if opcionRegiones == "Arica y Parinacota":
  print("region de Arica y Parinacota")
if opcionRegiones =="Antofagasta":
  print("Region de Antofagasta")
if opcionRegiones == "Atacama":
  print("Region de Atacama")
if opcionRegiones =="Coquimbo":
  print("Region de Coquimbo ")
if opcionRegiones =="Valparaiso":
  print("Region de Valparaiso")
if opcionRegiones == "Metropolitana":
  print("Region Metropolitana")
if opcionRegiones =="O’Higgins":
  print("Region de O’Higgins")
if opcionRegiones =="Maule":
  print("Region del Maule")
if opcionRegiones == "Ñuble":
  print("Region del Ñuble")
if opcionRegiones == "Biobío":
  print("Region del Biobío")
if opcionRegiones == "Araucanía":
  print("region de la Araucanía")
if opcionRegiones == "Los Ríos":
  print("Region de los Los Ríos")
if opcionRegiones == "Los Lagos":
  print("Region de Los Lagos")
if opcionRegiones == "Aysén":
  print("Region de Aysén")
if opcionRegiones == "Magallanes":
  print("Region de Magallanes")

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

##Grafico 

dias = ["1", "2", "3" , "4", "5", "6", "7" , "8" , "9" , "10" , "11" , "12" ,"13" , "14" ] 
casos = [11 , 44, 35 , 24 , 13, 43, 32,32 , 34, 43, 34 , 12 , 25 ,35 ] 
colors = ["red", "blue" , "green" , "black" , "blue" , "blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,"blue" ,] 
plt.title("Casos Sin Sintomas 2 semanas?")
plt.bar(dias, height=casos, color=colors)
plt.show()

