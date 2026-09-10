class Articulo:

    def __init__(self, descripcion, costo_unitario, unidades):
        self.descripcion = descripcion
        self.costo_unitario = costo_unitario
        self.unidades = unidades

    def calcular_subtotal(self):
        return self.costo_unitario * self.unidades

    def mostrar_detalle(self):
        print(f"Artículo: {self.descripcion}")
        print(f"Costo unitario: ${self.costo_unitario:.2f}")
        print(f"Unidades: {self.unidades}")
        print(f"Subtotal: ${self.calcular_subtotal():.2f}")


# --- Programa principal ---
if __name__ == "__main__":
    # Creación de dos artículos
    articulo1 = Articulo("Teclado Mecánico", 45.50, 2)
    articulo2 = Articulo("Monitor 24 pulgadas", 150.00, 3)

    # Mostrar detalle y subtotal del primer artículo
    print("--- Artículo 1 ---")
    articulo1.mostrar_detalle()
    print(f"Subtotal obtenido: ${articulo1.calcular_subtotal():.2f}\n")

    # Mostrar detalle y subtotal del segundo artículo
    print("--- Artículo 2 ---")
    articulo2.mostrar_detalle()
    print(f"Subtotal obtenido: ${articulo2.calcular_subtotal():.2f}")