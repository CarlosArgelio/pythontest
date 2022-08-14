#Escribir un programa que pida al usuario una 
#palabra y la muestre por pantalla 10 veces.

def run():
    word = input("Ingresa 1 palabra: ")
    for i in range(10):
        print(word)


if __name__ == '__main__':
    run()