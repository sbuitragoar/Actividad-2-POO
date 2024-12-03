class Esferas:
    __esferas_clases = {'A': 1, 'B': 2, 'C':3, 'D': 4} # referencias pesos de esferas
    @staticmethod
    def determinar_pesos(peso_esferas):
        if peso_esferas[0] == peso_esferas[1] and peso_esferas[0] == peso_esferas[2]:
            print("la esfera D es la diferente")
            if peso_esferas[3] > peso_esferas[0]:
                print("y de mayor peso")
            else:
                print("y de menor peso")
        elif peso_esferas[0] == peso_esferas[1] and peso_esferas[0] == peso_esferas[3]:
            print("la esfera C es la diferente")
            if peso_esferas[2] > peso_esferas[0]:
                print("y de mayor peso")
            else:
                print("y es de menor peso")      
        elif peso_esferas[0] == peso_esferas[2] and peso_esferas[0] == peso_esferas[3]:
            print("la esfera B es la diferente")
            if peso_esferas[1] > peso_esferas[3]:
                print("y de mayor peso")
            else:
                print("y es de menor peso")
        else:
            print("la esfera A es la diferente")
            if peso_esferas[0] > peso_esferas[1]:
                print("y de mayor peso")
            else:
                print("y es de menor peso")
       
peso_esferas = input("ingrese el peso de cada esfera separado por un espacio: ").split(" ")
pesos_formateados = list(map(int, peso_esferas))


esferas_ejemplo = Esferas()
esferas_ejemplo.determinar_pesos(pesos_formateados)
