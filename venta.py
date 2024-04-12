class Venta:
    def __inti__( self, libr_vend, stok_vend ):
        self.libro_vendido = libr_vend
        self.stock_vendido = stok_vend

    def obtnr_lib_vend( self ):
        return self.libro_vendido
    
    def obtnr_stok_vend( self ):
        return self.stock_vendido