class Compra:
   
    def __init__(self, valor_compra, color_bolita):
        self.valor_compra = valor_compra
        self.color_bolita = color_bolita.lower()
        self.porcentaje_descuento = 0
        self.valor_pagar = 0
        self.pagar()
       
    def pagar(self):
        if self.color_bolita == "blanco":
            self.porcentaje_descuento = 0
        elif self.color_bolita == "verde":
            self.porcentaje_descuento = 10
        elif self.color_bolita == "amarillo":
            self.porcentaje_descuento = 25
        elif self.color_bolita == "azul":
            self.porcentaje_descuento = 50
        else:
            self.porcentaje_descuento = 100
        self.valor_pagar = int(self.valor_compra - self.porcentaje_descuento * self.valor_compra / 100)
       
    def __str__(self):
        cadena = "El cliente debe pagar $" + str(self.valor_pagar)
        return cadena        
       
valor_compra = int(input("ingrese el valor de la compra: "))
color_bolita = input("ingrese el color de la bolita: ")


compra_ejemplo = Compra(valor_compra, color_bolita)
print(compra_ejemplo)
