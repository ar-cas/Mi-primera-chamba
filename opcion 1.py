
opcion=1
#En un ciclo while realiza operaciones hasta que el usuario escriba 0
while opcion!=0:
    num1=int(input("ingresa el primer numero"))
    num2=int(input("ingrsa el segundo numero"))
    print("ingresa 1. Sumar")
    print("ingresa 2. Resatar")
    print("ingresa 3. Multiplicar")
    print("ingresa 4. Dividir")
    op=int(input("¿Que operecion quieres hacer con esos numeros?"))
    if (op==1):
        resultado=num1+num2
        print("la suma de los numeros es:", resultado)
    elif(op==2):
        resultado=num1-num2
        print("la resta de los numero es:", resultado)
    elif(op==3):
        resultado=num1*num2
        print("la multiplicacion de los numeros es :", resultado)
    elif(op==4):
        resultado=num1/num2
        print("la divison de los numeros es:", resultado)
    else:
        print("no valido")
    opcion=int(input("deseas continuar, si no presiona 0. para salir"))
