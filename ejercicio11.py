class Numeros:
    @staticmethod
    def clasificar_numeros(numero_1, numero_2, numero_3):
        if(numero_1 > numero_2 and numero_1 > numero_3):
            print(f"el numero {numero_1} es mayor que los numeros {numero_2} y {numero_3}")
        elif(numero_2 > numero_1 and numero_2 > numero_3):
            print(f"el numero {numero_2} es mayor que los numeros {numero_1} y {numero_3}")
        elif(numero_3 > numero_1 and numero_3 > numero_2):
            print(f"el numero {numero_3} es mayor que los numeros {numero_1} y {numero_2}")
        else:
            print("estos numeros son todos iguales")
               
numero_1 = int(input("por favor ingrese el numero 1: "))
numero_2 = int(input("por favor ingrese el numero 2: "))
numero_3 = int(input("por favor ingrese el numero 3: "))


Numeros.clasificar_numeros(numero_1, numero_2, numero_3)
