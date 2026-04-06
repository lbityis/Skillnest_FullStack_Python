''' ACTIVIDAD: Gestor de inventario'''

# 1.- Crear una lista llamada inventario que contenga los siguientes articulos: Laptop, raton, monitor, cable hdmi.
inventario = ["Laptop", "raton", "monitor", "cable hdmi"]
print(f"1.- {inventario}")

# 2.- Utiliza el metodo correspondiente para agregar "impresora" y "teclado" al final de la lista.
inventario.append("impresora") 
inventario.append("teclado") 
print(f"2.- {inventario}")

# 3.- Utiliza la funcion integrada para mostrar cuantos elementos totales hay en la lista.
print(f"3.- {len(inventario)}")

# 4.- Modifica "teclado" por "teclado mecanico".
inventario[5] = "teclado mecanico"
print(f"4.- {inventario}")

# 5.- Crea una nueva lista llamada "promocion" que contenga los 3 primeros elementos de "inventario".
promocion = inventario[:3] 
print(f"5.- {promocion}")

# 6.- Mostrar la lista de inventario ordenado alfabeticamente.
inventario.sort()
print(f"6.- {inventario}")

# 7.- Elimina el ultimo elemento de la lista inventario mostrando el elemento eliminado y la lista final
eliminado = inventario.pop()
print(f"7.- Articulo eliminado: {eliminado}, Lista final: {inventario}")
