opcion=1
# hola vienvenido al programa
while opcion!=0:
    print("hola bienvenido al programa")
    print("ingresa 1. area del triangulo")
    print("ingresa 2. area del rectanfulo")
    print("ingresa 3. area del circulo")
    print("ingresa 4. convertir temperatura F a C")
    print("ingresa 5. convertir temperatura C a F")
    op=int(input("¿que quieres realizar?"))



    if(op==1):
        ingresa=("area del triangulo")
        base= float(input("ingresa la base del triangulo:"))
        altura= float(input("ingresa la altura del triangulo:"))
        area=(base*altura)/2
    elif(op==2):
        ingresar=("area del rctamgulo")
        base= float(input("ingresa la base del rectangulo:"))
        altura= float(input("ingresa la altura del rectangulo:"))
        area=(base*altura)
    elif(op==3):
        ingresar=("area del circulo") 
        radio=float(input("ingresa el radio del circulo:"))
        area=(base*altura)
        area=(3.14*radio**2)
    elif(op==4):
        ingresar=("convertir la temperatura F a C")
        fahrenheit=float(input("ingresa los grados en f:"))
        res=(fahrenheit-32)*5/9
        print("la temperatura en F es:",res)

    elif(op==5):
        ingresar=("convertir la temperatura C a F")
        celsius=float(input("ingresa los grados en C:"))
        res=(celsius*9/5)+32
        print("la temperatura en C es:",res)

    else:
        print("no valido")
    opcion=int(input("deseas continuar, si no presiona 0. para salir"))


    



