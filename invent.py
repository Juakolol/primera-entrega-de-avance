class Inventario:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def actualizar_inventario(self, libro, cantidad):
        for libro_inventario in self.libros:
            if libro_inventario == libro:
                libro_inventario.cantidad += cantidad
                break

    def registrar_venta(self, venta):
        libro_vendido = venta.libro
        cantidad_vendida = venta.cantidad_vendida
        for libro_inventario in self.libros:
            if libro_inventario == libro_vendido:
                libro_inventario.cantidad -= cantidad_vendida
                break

    def obtener_libros(self):
        return self.libros
