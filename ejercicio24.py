class Esferas:
    @staticmethod
    def determinar_pesos(peso_esferas):
        esferas = {0: 'A', 1: 'B',  2: 'C'}
        print("la esfera mas pesada es: ", esferas.get(peso_esferas.index(max(peso_esferas))))
       
peso_esferas = input("ingrese el peso de cada esfera separado por un espacio: ").split(" ")
pesos_formateados = list(map(int, peso_esferas))


esferas_ejemplo = Esferas()
esferas_ejemplo.determinar_pesos(pesos_formateados
