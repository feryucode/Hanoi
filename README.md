# Hanoi

## Estructura del código (Funciones)

El programa está dividido en **4 funciones** principales:

1. **`limpiar_pantalla()`**: Limpia la consola usando `cls` (en Windows) o `clear` (en Linux/Mac) antes de mostrar el siguiente movimiento, para que la animación se vea en el mismo lugar y no se llene la pantalla de texto.
2. **`imprimir_torres(torres, num_discos)`**: Dibuja los postes A, B y C en la terminal representando los discos con asteriscos (`*`). También incluye un `time.sleep` para hacer una pequeña pausa entre cada paso y que alcance a verse cómo se mueven.
3. **`mover_disco(torres, origen, destino, num_discos)`**: Hace el cambio en las listas; saca el disco de arriba del poste origen con `.pop()` y lo mete en el poste destino con `.append()`. Si el modo visual está activado, llama a `imprimir_torres` para actualizar el dibujo.
4. **`hanoi_animado(n, origen, auxiliar, destino, torres, num_discos)`**: Es la función recursiva que resuelve el algoritmo. Se va llamando a sí misma para acomodar los discos entre los postes hasta llegar al caso base (`n == 1`).
