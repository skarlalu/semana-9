Estudiante: Karla Daniela Luque Navarrete

Descripción del Sistema
Este proyecto es un sistema de administración básico para un restaurante desarrollado en Python. Su objetivo es gestionar productos y usuarios aplicando una arquitectura modular y utilizando las estructuras de datos nativas del lenguaje de forma justificada.

Estructura del Proyecto y Responsabilidades
El proyecto está dividido en capas para separar la lógica de los datos y la interfaz:
* modelos/producto.py: Contiene la clase `Producto`, encargada de representar la información de cada artículo (código, nombre, categoría, precio).
* modelos/usuario.py: Contiene la clase `Usuario`, encargada de representar los datos de las personas registradas (identificación, nombre, correo).
* servicios/restaurante.py: Contiene la clase `Restaurante`, responsable de administrar las colecciones y la lógica de negocio (registrar, buscar, actualizar, eliminar y listar).
* main.py: Es el punto de arranque del programa. Muestra el menú interactivo, solicita los datos al usuario y se comunica con el servicio.

Uso de Estructuras de Datos
Cada estructura se implementó para resolver una necesidad específica del sistema:
* Listas (`list`):** Utilizadas en el servicio (`restaurante.py`) para almacenar las colecciones de productos y usuarios. Son ideales porque estas colecciones son dinámicas y necesitan crecer, reducirse o modificarse constantemente.
* Tuplas (`tuple`):** Utilizada en `main.py` para definir las opciones del menú principal. Al ser una estructura inmutable, garantiza que los textos del menú se mantengan estables y no se modifiquen por accidente durante la ejecución.
* Diccionarios (`dict`):** Utilizado en `main.py` para relacionar el número de la opción seleccionada (clave) con la función que debe ejecutarse (valor). Esto optimiza el código al evitar largas cadenas de condicionales `if-elif`.
* Conjuntos (`set`):** Utilizado en el servicio para obtener las categorías de los productos registrados. Gracias a su naturaleza matemática, el conjunto elimina automáticamente cualquier categoría duplicada para mostrar una lista limpia.

Instrucciones de Ejecución
1. Abra una terminal y asegúrese de estar en el directorio principal del proyecto (`restaurante_app/`).
2. Ejecute el comando: `python main.py`
3. Siga las instrucciones del menú interactivo ingresando el número de la opción deseada.

Seleccionar la estructura de datos adecuada es fundamental para optimizar el rendimiento y la legibilidad del código. Usar listas para datos mutables, tuplas para constantes, diccionarios para búsquedas rápidas por clave y conjuntos para garantizar valores únicos permite que el software resuelva problemas de la vida real de manera más eficiente, segura y con un código mucho más limpio.