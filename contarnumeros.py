print ("Initializaing")

numero = 1
apellido = "4.5"
numeroFlotante = 4.65
booleano = False
print(type(numero))
print(type(numeroFlotante))
print(type(apellido))
print(type(booleano))

numero2 = float(apellido)
print(numero2)
 

print(isinstance(numeroFlotante,float))
print(isinstance(numero2,float))

nombre = input("Ingrese su nombre: ")
print("Hola "+ nombre)

if(isinstance(numero,int)):
    print("Varible entera")

    numeroFlotante += 4.6 
    apellido = input("Ingrese su apellido: ")
    print("Nombre completo: "+nombre+" "+apellido)
    edadstr = input("Ingrese su edad: ")
    edad = int(edadstr)
    
    if(edad>20):
        print("Edad correcta")
    booleano = True
    print(booleano)
    print("Programa finalizado")

    for i in range(10,20,2):
       print ("Repeating...")
    if i== 15:
        i+=3
    print(i)

print("")


j = 0

while j < 6:
  print(j)
  if j == 2: 
    j=4
  j += 1


j = 1

while True:
  print(j)
  if j == 10:
     break;
     j += 1