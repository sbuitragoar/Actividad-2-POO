class Triangulo_Equilatero:
   
    def __init__(self, lado):
        self.lado = lado
       
    def perimetro(self):
        self.perimetro = self.lado*3
        return self.perimetro
       
    def altura(self):
        self.altura = self.lado * math.sqrt(3)/2
        return round(self.altura, 1)
       
    def area(self):
        self.area = (self.lado**2) * math.sqrt(3)/4
        return round(self.area, 1)
       
    def mostrar_caracteristicas(self):
        print(f"el perimetro es {self.perimetro()} cm, su altura {self.altura()} cm y su area {self.area()} cm^2")
   
lado = int(input("por favor ingrese el tamaño del lado del triangulo: "))
triangulo_ejemplo = Triangulo_Equilatero(lado)
triangulo_ejemplo.mostrar_caracteristicas()
