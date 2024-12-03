class Trabajador:
    def __init__(self, nombres, horas_trabajadas, valor_hora, horas_extra = 0, horas_extra_8 = 0):
        self.nombres = nombres
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.salario = 0
        self.calcular()
       
    def calcular(self):
        if(self.horas_trabajadas > 0):
            self.horas_extra = self.horas_trabajadas - 40
            if(self.horas_extra > 8):
                self.horas_extra_8 = self.horas_extra - 8
                self.salario = 40 * self.valor_hora + 16 * self.valor_hora + self.horas_extra_8 * 3 * self.valor_hora
            else:
                self.salario = 40 * self.valor_hora + self.horas_extra * 2 * self.valor_hora
        else:
            sefl.salario = self.horas_trabajadas * self.valor_hora
        print(f"El trabajador {self.nombres} devengo ${self.salario}")
       
nombres_trabajador = input("ingrese el nombre por favor: ")
horas_trabajadas = int(input("ingrese las horas trabajadas: "))
valor_hora = int(input("ingrese el pago por hora: "))
   


trabajador_ejemplo = Trabajador(nombres_trabajador, horas_trabajadas, valor_hora)
