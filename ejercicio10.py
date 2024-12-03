class Estudiante:
    # esto lo hize porque quize hacerlo adicional para registrar cuantos inscritos ha habido y practicas atributos de clase
    numeros_inscritos = 0
    pago_matricula_base = 50000
   
    def __init__(self, numero_inscripcion, nombres, patrimonio, estrato_social):
        self.numero_inscripcion = numero_inscripcion
        self.nombres = nombres
        self.patrimonio = patrimonio
        self.estrato_social = estrato_social
        self.pago_mat = 0
        Estudiante.registro()
   
    def pago_matricula(self):
        if(self.patrimonio > 2000000 and self.estrato_social>3):
            self.pago_mat =  int(Estudiante.pago_matricula_base + 0.03 * self.patrimonio)
        else:
            self.pago_mat = Estudiante.pago_matricula_base
           
        print(f"el estudiante con numero de inscripcion {self.numero_inscripcion} y nombre {self.nombres} debe pagar ${self.pago_mat}")
    @classmethod
    def registro(cls):
        cls.numeros_inscritos = cls.numeros_inscritos + 1
       
numero_inscripcion = input("ingrese el numero de inscripcion: ")
nombres = input("ingrese los nombres: ")
patrimonio = int(input("ingrese el patrimonio: "))
estrato_social = int(input("ingrese el estrato social: "))


estudiante_ejemplo = Estudiante(numero_inscripcion, nombres, patrimonio, estrato_social)
estudiante_ejemplo.pago_matricula()
