class Desastre_natural:
    def __init__(self,lugar,naturaleza,peligrosidad,duracion):
        self.lugar = lugar
        self.naturaleza = naturaleza
        self.peligrosidad = peligrosidad
        self.duracion = duracion
 
    def destruir(self):
        print(f"estoy destruyendo por medio de {self.naturaleza}")
 
    def iniciar(self):
        print(f"Estoy iniciando en {self.lugar}")
 
    def terminar(self):
        print(f"Se terminó el desastre natural en {self.duracion} horas")
 
 
inundacion = Desastre_natural("sabaneta","deslizamiento",4,72)
inundacion.iniciar()
inundacion.destruir()
inundacion.terminar()
