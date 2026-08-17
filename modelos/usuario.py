class Usuario:
    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    def __str__(self) -> str:
        return f"[{self.identificacion}] {self.nombre} | Correo: {self.correo}"