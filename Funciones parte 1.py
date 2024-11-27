# Crear funciones 

#Funcion llamada saludar, va a recibir el nombre 
def saludar(nombre):
    print("holaaaa",nombre)

nombre=input("ingresa  tu nombre")
saludar(nombre)



#Funcion llamada sumita, va a recibir 5 numeros 
#Va a crear el valor de la suma
def sumita(n1,n2,n3,n4,n5):
    res_suma=n1+n2+n3+n4+n5
    return res_suma 

num1=int(input("ingresa el primer numero"))
num2=int(input("ingresa el segundo numero"))
num3=int(input("ingresa el tercero numero"))
num4=int(input("ingresa el cuarto numero"))
num5=int(input("ingresa el quinto numero"))

#Mandar llamar la funcion 
print(sumita(num1,num2,num3,num4,num5))

#Crear una funcion llamada area_triangulo 
#Que reciba base  y altura
#Regrese el resultado del area 

def area_triangulo(b,h):
    area=(b*h)/2
    return area
#Buscar la funcion 
print(area_triangulo(4,5))

#Crear una multiplicacion 
def multiplicar(num1num2b,num3):
    return num1*num2*num3
resultado=multiplicar(2,4,3)
print(resultado)

def largo_cadena(texto):
    return 




#Pedir calif , primer y segundo parcial
def promedio(calif1,calif2):
    return (calif1+calif2)/2
 #Pedir las calificaciones 
calif1=float(input("ingresa la primera calificacion :"))
calif2=float(input("ingresa la segunda calificacion :"))
#Calcular y mostrar el resultado
print("el promedio es:",promedio(calif1,calif2))

def disk_curp(nombre,edad,mes):


                                           