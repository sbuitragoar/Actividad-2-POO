import math
from abc import ABC, abstractmethod
import math


# Clase base abstracta - clase padre - debido a que es abstracta no puede ser instanciada
class Figura(ABC):
    @abstractmethod
    def calcularArea(self):
        pass
   
    @abstractmethod
    def calcularPerimetro(self):
        pass


# las clases hijas deben implementar los metodos calcularArea y calcularPerimetro


class Circulo(Figura):
    def __init__(self, radio: int):
        self.radio = radio
   
    @property # esto como un getter es decir cuando hacemos algo como print(self.radio)
    def radio(self):
        return self._radio
   
    @radio.setter # esto es un setter con el cual estamos verificando que el radio no es negativo
    def radio(self, valor: int):
        if valor <= 0:
            raise ValueError("El radio debe ser un numero positivo")
        self._radio = valor
       
    def calcularArea(self) -> float:
        return math.pi * math.pow(self.radio, 2)
   
    def calcularPerimetro(self) -> float:
        return 2 * math.pi * self.radio
   
class Rectangulo(Figura):
    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura
       
    @property
    def base(self):
        return self._base    
    @property
    def altura(self):
        return self._altura
   
    @base.setter
    def base(self, valor: int):
        if valor <= 0:
            raise ValueError("La base debe ser un numero positivo")
        self._base = valor
   
    @altura.setter
    def altura(self, valor: int):
        if valor <= 0:
            raise ValueError("La altura debe ser un numero positivo")
        self._altura = valor
       
    def calcularArea(self) -> float:
        return self.base * self.altura
   
    def calcularPerimetro(self) -> float:
        return (2 * self.base) + (2 * self.altura)
       
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
   
    @property
    def lado(self):
        return self._lado
   
    @lado.setter
    def lado(self, valor: int):
        if valor <= 0:
            raise ValueError("El lado debe ser un numero positivo")
        self._lado = valor


    def calcularArea(self) -> float:
        return self.lado * self.lado
   
    def calcularPerimetro(self) -> float:
        return 4 * self.lado


class TrianguloRectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
       
    @property
    def base(self):
        return self._base
   
    @property
    def altura(self):
        return self._altura
   
    @base.setter
    def base(self, valor: int):
        if valor <= 0:
            raise ValueError("La base debe ser un numero positivo")
        self._base = valor
   
    @altura.setter
    def altura(self, valor: int):
        if valor <= 0:
            raise ValueError("El lado debe ser un numero positivo")
        self._altura = valor
   
    def calcularArea(self) -> float:
        return (self.base * self.altura ) / 2
   
    def calcularPerimetro(self) -> float:
        return self.base + self.altura + self.calcularHipotenusa()


    def calcularHipotenusa(self) -> float:
        return math.pow(self.base*self.base + self.altura*self.altura, 0.5)


    def determinarTipoTriangulo(self) -> None:
        if self.base == self.altura and self.base == self.calcularHipotenusa() and self.altura == self.calcularHipotenusa():
            print("Es un triangulo equilatero\n")
        elif self.base != self.altura and self.base != self.calcularHipotenusa() and self.altura != self.calcularHipotenusa():
            print("Es un triangulo escaleno\n")
        else:
            print("Es un triangulo isosceles\n")


# en python no es necesario crear un clase principal como en java
if __name__ == "__main__":
    # pero si utilizamos este condicional para hacer pruebas es decir para comprobar que estamos corriendo el codigo directamente no desde un modulo
    figura_1 = Circulo(2)
    figura_2 = Rectangulo(1,2)
    figura_3 = Cuadrado(3)
    figura_4 = TrianguloRectangulo(3, 5)
   
    print(f"El area del circulo es = {figura_1.calcularArea()}")
    print(f"El perimetro del circulo es= {figura_1.calcularPerimetro()}\n")
   
    print(f"El area del rectangulo es = {figura_2.calcularArea()}")
    print(f"El perimetro del rectangulo es= {figura_2.calcularPerimetro()}\n")
   
    print(f"El area del cuadrado es = {figura_3.calcularArea()}")
    print(f"El perimetro del cuadrado es= {figura_3.calcularPerimetro()}\n")
   
    print(f"El area del triangulo es = {figura_4.calcularArea()}")
    print(f"El perimetro del triangulo es= {figura_4.calcularPerimetro()}")
   
    figura_4.determinarTipoTriangulo()
