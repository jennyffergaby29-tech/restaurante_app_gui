class Producto:
    def __init__(self, id_producto: int, nombre: str, precio: float, stock: int):
        self.id = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(
            id_producto=datos.get("id", 0),
            nombre=datos.get("nombre", ""),
            precio=float(datos.get("precio", 0.0)),
            stock=int(datos.get("stock", 0))
        )