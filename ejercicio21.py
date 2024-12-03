import math


class Triangulo:
   
    def __init__(self, lado_1, lado_2, lado_3):
        self.lado_1 = lado_1
        self.lado_2 = lado_2
        self.lado_3 = lado_3
       
    def comprobar_lados(self):
        if((self.lado_1 + self.lado_2 <= self.lado_3) or (self.lado_1 + self.lado_3 <= self.lado_2) or (self.lado_2 + self.lado_3 <= self.lado_1)):
            return False
        else:
            return True
       
    def perimetro(self):
        self.perimetro = self.lado_1 + self.lado_2 + self.lado_3
        return round(self.perimetro, 1)
       
    def semiperimetro(self):
        self.semiperimetro = self.perimetro/2
        return round(self.semiperimetro, 1)
       
    def area(self):
        if (self.lado_1 == self.lado_2 == self.lado_3):
            self.area = self.lado_1**2 * math.sqrt(3)/4
           
        elif (self.lado_1 == self.lado_2) or (self.lado_1 == self.lado_3) or (self.lado_2 == self.lado_3):
            if self.lado_1 == self.lado_2:
                self.area = (self.lado_3* math.sqrt(self.lado_1**2 - ((self.lado_3)/2)**2)) / 2
            elif self.lado_1==self.lado_3:
                self.area = (self.lado_2*math.sqrt(self.lado_1**2 - ((self.lado_2)/2))**2) / 2
            else:
                self.area = (self.lado_1*math.sqrt(self.lado_2**2 - ((self.lado_1)/2))**2) / 2
        else:
            # formula de heron
            self.area = math.sqrt(self.semiperimetro*(self.semiperimetro-self.lado_1)*(self.semiperimetro-self.lado_2)*(self.semiperimetro-self.lado_3))
        return round(self.area, 1)
       
    def mostrar_caracteristicas(self):
        if(self.comprobar_lados()):
            print(f"el perimetro es {self.perimetro()} cm, su semiperimetro {self.semiperimetro()} cm y su area {self.area()} cm^2")
        else:
            print("lo lamento este triangulo no cumple con las caracteristicas estandar de un triangulo")


lado_1 = int(input("ingrese tamaño del lado 1: "))
lado_2 = int(input("ingrese tamaño del lado 2: "))
lado_3 = int(input("ingrese tamaño del lado 3: "))


triangulo_ejemplo = Triangulo(lado_1, lado_2, lado_3)
triangulo_ejemplo.mostrar_caracteristicas()
