class Dispositivo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_detalles(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")


class Telefono(Dispositivo):

    def __init__(self, marca, modelo, numero_camaras):
        super().__init__(marca, modelo)
        self.numero_camaras = numero_camaras

    def mostrar_detalles(self):
        print(
            f"Teléfono -> Marca: {self.marca}, Modelo: {self.modelo}, Cámaras: {self.numero_camaras}"
        )


class Computador(Dispositivo):

    def __init__(self, marca, modelo, ram_gb):
        super().__init__(marca, modelo)
        self.ram_gb = ram_gb

    def mostrar_detalles(self):
        print(
            f"Computador -> Marca: {self.marca}, Modelo: {self.modelo}, RAM: {self.ram_gb} GB"
        )


# --- Creación de objetos y ejecución del método ---
if __name__ == "__main__":
    mi_telefono = Telefono("Samsung", "Galaxy S23", 3)
    mi_computador = Computador("Lenovo", "ThinkPad X1", 16)

    mi_telefono.mostrar_detalles()
    mi_computador.mostrar_detalles()