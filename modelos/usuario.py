class Usuario:
    def __init__(self, username: str, password: str, rol: str):
        self.username = username
        self.password = password
        self.rol = rol

    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(
            username=datos.get("username", ""),
            password=datos.get("password", ""),
            rol=datos.get("rol", "Usuario")
        )