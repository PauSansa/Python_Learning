class Producto:
    precio = 0
    IVA = 21
    nombre = ""

    def __init__(self, precio, nombre):
        self.precio = precio
        self.nombre = nombre

    def aplicarDescuento(self, descuento):
        precioDescontado = self.precio - (self.precio * (descuento/100))
        return precioDescontado

    def aplicarIVA(self):
        precioConIva = self.precio + (self.precio * self.IVA / 100)
        return precioConIva

nombre = input("Di el nombre del producto: ")
precio =int(input("Pon el precio del producto: "))
producto = Producto(precio, nombre)
print(producto.aplicarIVA())
