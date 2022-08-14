#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

def run():
    n = int(input("Coloca un numero entero positivo: "))
    for i in range(1, n+1, 2) #quitar 1 a n 
        print()

if __name__=='__main__':
    run()