class Libro:
    def __init__( self, tit, aut, pre, stok):
        self.titulo = tit
        self.autor = aut
        self.precio = pre
        self.cantidad_de_libros = stok

    def actualizar_precio( self, precio_nuevo):
        self.nuevo_precio = precio_nuevo

    def acutalizar_stock( self, actualizar_stock):
        self.nuevo_stock = actualizar_stock

    def obtnr_titulo( self ):
        return self.titulo
    
    def obtnr_autor( self ):
        return self.autor
    
    def obtnr_precio( self ):
        return self.precio
    
    def obtnr_cantidad( self ):
        return self.cantidad_de_libros