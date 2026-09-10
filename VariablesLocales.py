class Animal:
    def _init_(self, nombre, edad, especie):
        self.color = 
        self.precio = precio
        self.marca = marca
        self.tamano = tamano
        self.sabor = sabor
        self.caducidad = caducidad
        self.peso = peso
        self.tabla_nutricional = tabla_nutricional
        self.cantidad = 0
        self.disponible = False

    def vender(self,cantidad_vendidos):
        if (cantidad_vendidos <= self.cantidad):
            print(f"Se vendieron {cantidad_vendidos} {self.nombre}")
            self.cantidad -= cantidad_vendidos
            self.mostrar_info()
        else:
            print("La cantidad que se quiere vender no esta disponible")

        if (self.cantidad == 0):
            self.disponible = False 

    def agregar(self,cantidad_agregar):
        if (cantidad_agregar>0):
            self.cantidad += cantidad_agregar
            self.disponible = True
            print(f"Se agregaron {cantidad_agregar} {self.nombre}")
            self.mostrar_info()
        else:
            print("no se puede agregar una cantidad menor que cero")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Marca: {self.marca}")
        print(f"Tamaño: {self.tamano}")
        print(f"Peso: {self.peso}")
        print(f"Sabor: {self.sabor}")         
        print(f"Tabla nutricional: {self.tabla_nutricional}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Disponible: {self.disponible}")                               
                                
enlatado1 = Producto("atún",
                     "7000$",
                     "Vancamps",
                     "personal",
                     "salado",
                     "30/septiembre/2026",
                     "0.5Kg",
                     ["Proteina: 20mg",
                      "Sodio: 100mg",
                      "Calorias: 200kcal"],
                      )
enlatado1.mostrar_info()
enlatado1.agregar(12)
enlatado1.vender(4)