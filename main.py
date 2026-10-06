#Ejercicio 1
def pedir_nombre():
    nombre=input("Introduce tu nombre: ")
    print ("Hola", nombre)

#Ejercicio 2
def operaciones():
    num1=int(input("Dime el primer numero: "))
    num2=int(input("Dime el segundo numero: "))

    suma=num1+num2
    resta=num1-num2
    mult=num1*num2
    div=num1/num2

    print("Suma:", suma)
    print("Resta:", resta)
    print("Multiplicación:", mult)
    print("División:", div)

#Ejercicio 3
def area_rectangulo():
    b=int(input("Base: "))
    h=int(input("Altura: "))

    a=b*h

    print("El area del rectangulo es:", a)

#Ejercicio 4
def grados():
    cel=input("Temperatura en Celsius: ")
    farenh=cel*9/5+32
    print()









if __name__ == "__main__":
    grados()