# VARIABLES GLOBALES
Productos = {1: 'Pantalones', 2: 'Camisas', 3: 'Corbatas', 4: 'Casacas'}
Precios = {1: 200.00, 2: 120.00, 3: 50.00, 4: 350.00}
Stock = {1: 50, 2: 45, 3: 30, 4: 15}

# FUNCIONES DEL SISTEMA
def mostrar_inventario():
    """Muestra el inventario actual con un formato tabular básico."""
    print("\n" + "="*40)
    print("Lista de Productos:")
    print("="*40)
    # Encabezados de columnas alineados
    print(f"{'ID':<4} | {'Nombre':<12} | {'Precio':<8} | {'Stock':<5}")
    print("-" * 40)
    for key in Productos:
        print(f"{key:<4} | {Productos[key]:<12} | {Precios[key]:<8.2f} | {Stock[key]:<5}")
    print("="*40)

def agregar_producto():
    """Solicita datos al usuario y agrega un nuevo producto a los diccionarios."""
    print("\n--- AGREGAR PRODUCTO ---")
    try:
        nuevo_id = int(input("Ingrese el ID del nuevo producto: "))
        if nuevo_id in Productos:
            print("Error: ¡Ese ID ya existe en el sistema!")
            return # Sale de la función si hay error
        
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio: "))
        stock = int(input("Ingrese la cantidad en stock: "))
        
        Productos[nuevo_id] = nombre
        Precios[nuevo_id] = precio
        Stock[nuevo_id] = stock
        print("Producto agregado exitosamente")
    except ValueError:
        print("Error: Debe ingresar valores numéricos para ID, precio y stock.")

def eliminar_producto():
    """Elimina un producto de los diccionarios usando su ID."""
    print("\n--- ELIMINAR PRODUCTO ---")
    try:
        id_eliminar = int(input("Ingrese el ID del producto a eliminar: "))
        if id_eliminar in Productos:
            del Productos[id_eliminar]
            del Precios[id_eliminar]
            del Stock[id_eliminar]
            print("Producto eliminado exitosamente")
        else:
            print("Error: El ID ingresado no existe.")
    except ValueError:
        print("Error: El ID debe ser un número entero.")

def actualizar_producto():
    """Actualiza los datos de un producto existente."""
    print("\n--- ACTUALIZAR PRODUCTO ---")
    try:
        id_actualizar = int(input("Ingrese el ID del producto a actualizar: "))
        if id_actualizar in Productos:
            print(f"Editando: {Productos[id_actualizar]}")
            nombre = input("Ingrese el nuevo nombre: ")
            precio = float(input("Ingrese el nuevo precio: "))
            stock = int(input("Ingrese el nuevo stock: "))
            
            Productos[id_actualizar] = nombre
            Precios[id_actualizar] = precio
            Stock[id_actualizar] = stock
            print("¡Producto actualizado exitosamente!")
        else:
            print("Error: El ID ingresado no existe.")
    except ValueError:
        print("Error: Ingresó un valor no válido.")
# PROGRAMA PRINCIPAL (Menú)
def main():
    while True:
        mostrar_inventario()
        print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
        opcion = input("Elija una opción: ")
        
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            eliminar_producto()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            print("\nSaliendo del programa. Hasta luego\n")
            break
        else:
            print("\n Error: Opción no válida. Intente nuevamente.")

# Punto de entrada del script
if __name__ == "__main__":
    main()
