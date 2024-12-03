import math


class EcuacionSegundoGrado:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def calcular_raices(self):
        discriminante = self.b**2 - 4 * self.a * self.c
        if discriminante > 0:
            raiz1 = (-self.b + math.sqrt(discriminante)) / (2 * self.a)
            raiz2 = (-self.b - math.sqrt(discriminante)) / (2 * self.a)
            return raiz1, raiz2
        elif discriminante == 0:
            raiz = -self.b / (2 * self.a)
            return raiz,
        else:
            return None


a = float(input("Ingrese el valor de A: "))
b = float(input("Ingrese el valor de B: "))
c = float(input("Ingrese el valor de C: "))


ecuacion = EcuacionSegundoGrado(a, b, c)
soluciones = ecuacion.calcular_raices()


if soluciones:
    print("Las soluciones son:", soluciones)
else:
    print("La ecuación no tiene soluciones reales.")

