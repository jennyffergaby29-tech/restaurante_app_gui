from modelos.usuario import Usuario
from modelos.producto import Producto
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self, ruta_usuarios: str, ruta_productos: str):
        self._ruta_usuarios = ruta_usuarios
        self._ruta_productos = ruta_productos
        self._usuarios: list[Usuario] = []
        self._productos: list[Producto] = []
        self.cargar_datos()

    def cargar_datos(self):
        datos_usuarios = ArchivoServicio.cargar_json(self._ruta_usuarios)
        self._usuarios = [Usuario.desde_diccionario(u) for u in datos_usuarios]

        datos_productos = ArchivoServicio.cargar_json(self._ruta_productos)
        self._productos = [Producto.desde_diccionario(p) for p in datos_productos]

    def validar_acceso(self, username: str, password: str) -> Usuario | None:
        for u in self._usuarios:
            if u.username == username and u.password == password:
                return u
        return None

    def obtener_usuarios(self) -> list[Usuario]:
        return self._usuarios

    def obtener_productos(self) -> list[Producto]:
        return self._productos