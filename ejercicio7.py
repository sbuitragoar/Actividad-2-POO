class Jerarquia_Numberos:
    @staticmethod
    def clasificar_numeros(numero_A, numero_B):
        if(numero_A > numero_B):
            print(f"el numero {numero_A} es mayor que {numero_B}")
        elif(numero_A == numero_A):
            print(f"el numero {numero_A} es igual a {numero_B}")
        else:
            print(f"el numero {numero_A} es menor que {numero_B}")


A = int(input(“ingrese el numero 1: “))
B = int(input(“ingrese el numero 2:  “))


Jerarquia_Numberos.clasificar_numeros(A, B)
