from typing import List, Optional, Set
from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    def __init__(self) -> None:
        # Uso de LISTAS: Para almacenar y administrar colecciones dinámicas de objetos.
        self.productos: List[Producto] = []
        self.usuarios: List[Usuario] = []

    # --- GESTIÓN DE PRODUCTOS ---
    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo):
            return False  # El código ya existe
        self.productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_producto(self, codigo: str, nuevo_nombre: str, nueva_categoria: str, nuevo_precio: float) -> bool:
        producto = self.buscar_producto(codigo)
        if producto:
            producto.nombre = nuevo_nombre
            producto.categoria = nueva_categoria
            producto.precio = nuevo_precio
            return True
        return False

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto:
            self.productos.remove(producto)
            return True
        return False

    def listar_productos(self) -> List[Producto]:
        return self.productos

    # --- GESTIÓN DE USUARIOS ---
    def registrar_usuario(self, usuario: Usuario) -> bool:
        for u in self.usuarios:
            if u.identificacion == usuario.identificacion:
                return False  # Identificación ya registrada
        self.usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> List[Usuario]:
        return self.usuarios

    # --- OPERACIONES ADICIONALES ---
    def obtener_categorias_unicas(self) -> Set[str]:
        # Uso de CONJUNTO (set): Para obtener información sin elementos duplicados.
        categorias = set()
        for producto in self.productos:
            categorias.add(producto.categoria)
        return categorias