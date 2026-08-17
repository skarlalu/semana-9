import sys
from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

# Uso de TUPLA: Para información estable que no debe cambiar durante la ejecución
OPCIONES_MENU = (
    "========================================",
    "        SISTEMA DE RESTAURANTE",
    "========================================",
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "----------------------------------------",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "----------------------------------------",
    "8. Mostrar categorías",
    "9. Salir",
    "========================================"
)

def mostrar_menu():
    for linea in OPCIONES_MENU:
        print(linea)

# --- FUNCIONES DE INTERFAZ ---
def ui_registrar_producto(restaurante: Restaurante):
    codigo = input("Ingrese el código del producto: ").strip()
    nombre = input("Ingrese el nombre del producto: ").strip()
    categoria = input("Ingrese la categoría del producto: ").strip()
    
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio < 0:
            print("❌ El precio no puede ser negativo.")
            return
    except ValueError:
        print("❌ Error: Debe ingresar un valor numérico para el precio.")
        return

    producto = Producto(codigo, nombre, categoria, precio)
    if restaurante.registrar_producto(producto):
        print("✅ Producto registrado exitosamente.")
    else:
        print("❌ Error: Ya existe un producto con ese código.")

def ui_buscar_producto(restaurante: Restaurante):
    codigo = input("Ingrese el código a buscar: ").strip()
    producto = restaurante.buscar_producto(codigo)
    if producto:
        print("🔍 Producto encontrado:", producto)
    else:
        print("❌ Producto no encontrado.")

def ui_actualizar_producto(restaurante: Restaurante):
    codigo = input("Ingrese el código del producto a actualizar: ").strip()
    # Corrección realizada: usar 'not' en lugar de 'no'
    if not restaurante.buscar_producto(codigo):
        print("❌ Producto no encontrado.")
        return

    nombre = input("Ingrese el nuevo nombre: ").strip()
    categoria = input("Ingrese la nueva categoría: ").strip()
    
    try:
        precio = float(input("Ingrese el nuevo precio: "))
        if precio < 0:
            print("❌ El precio no puede ser negativo.")
            return
    except ValueError:
        print("❌ Error: Valor numérico inválido para el precio.")
        return

    if restaurante.actualizar_producto(codigo, nombre, categoria, precio):
        print("✅ Producto actualizado correctamente.")

def ui_eliminar_producto(restaurante: Restaurante):
    codigo = input("Ingrese el código del producto a eliminar: ").strip()
    if restaurante.eliminar_producto(codigo):
        print("✅ Producto eliminado exitosamente.")
    else:
        print("❌ Producto no encontrado.")

def ui_listar_productos(restaurante: Restaurante):
    productos = restaurante.listar_productos()
    if not productos:
        print("⚠️ No hay productos registrados.")
    else:
        print("\n--- Lista de Productos ---")
        for p in productos:
            print(p)

def ui_registrar_usuario(restaurante: Restaurante):
    identificacion = input("Ingrese identificación del usuario: ").strip()
    nombre = input("Ingrese el nombre del usuario: ").strip()
    correo = input("Ingrese el correo del usuario: ").strip()

    usuario = Usuario(identificacion, nombre, correo)
    if restaurante.registrar_usuario(usuario):
        print("✅ Usuario registrado exitosamente.")
    else:
        print("❌ Error: Ya existe un usuario con esa identificación.")

def ui_listar_usuarios(restaurante: Restaurante):
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("⚠️ No hay usuarios registrados.")
    else:
        print("\n--- Lista de Usuarios ---")
        for u in usuarios:
            print(u)

def ui_mostrar_categorias(restaurante: Restaurante):
    categorias = restaurante.obtener_categorias_unicas()
    if not categorias:
        print("⚠️ No hay categorías registradas.")
    else:
        print("\n--- Categorías Disponibles ---")
        for c in categorias:
            print(f"- {c}")

def ui_salir(restaurante: Restaurante):
    print("👋 Saliendo del sistema...")
    sys.exit(0)

# Uso de DICCIONARIO: Para asociar opciones con funciones
RUTAS_MENU = {
    '1': ui_registrar_producto,
    '2': ui_buscar_producto,
    '3': ui_actualizar_producto,
    '4': ui_eliminar_producto,
    '5': ui_listar_productos,
    '6': ui_registrar_usuario,
    '7': ui_listar_usuarios,
    '8': ui_mostrar_categorias,
    '9': ui_salir
}

def main():
    restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        accion = RUTAS_MENU.get(opcion)
        
        if accion:
            print("\n----------------------------------------")
            accion(restaurante)
            print("----------------------------------------\n")
        else:
            print("❌ Opción inválida. Intente de nuevo.\n")

if __name__ == "__main__":
    main()