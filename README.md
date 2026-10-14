# Hanoi

## Estructura del código (Funciones)

El programa está dividido en **4 funciones** principales:

1. **`limpiar_pantalla()`**: Limpia la consola usando `cls` (en Windows) o `clear` (en Linux/Mac) antes de mostrar el siguiente movimiento, para que la animación se vea en el mismo lugar y no se llene la pantalla de texto.
2. **`imprimir_torres(torres, num_discos)`**: Dibuja los postes A, B y C en la terminal representando los discos con asteriscos (`*`). También incluye un `time.sleep` para hacer una pequeña pausa entre cada paso y que alcance a verse cómo se mueven.
3. **`mover_disco(torres, origen, destino, num_discos)`**: Hace el cambio en las listas; saca el disco de arriba del poste origen con `.pop()` y lo mete en el poste destino con `.append()`. Si el modo visual está activado, llama a `imprimir_torres` para actualizar el dibujo.
4. **`hanoi_animado(n, origen, auxiliar, destino, torres, num_discos)`**: Es la función recursiva que resuelve el algoritmo. Se va llamando a sí misma para acomodar los discos entre los postes hasta llegar al caso base (`n == 1`).

## Resultados de los Tiempos

| Cantidad de Discos | Movimientos ($2^n - 1$) | Tiempo de Ejecución | Notas |
|---|---|---|---|
| **5 discos** | 31 | 0.39 segundos | Con el modo visual activado (imprimiendo los postes y pausas). |
| **10 discos** | 1,023 | 0.000124 segundos | Modo rápido (solo procesamiento en memoria, sin animación). |
| **30 discos** | 1,073,741,823 | ~2.2 minutos (Estimado) | Tomando como base la velocidad de los 10 discos (~133 segundos). |
| **64 discos** | 18,446,744,073,709,551,615 | ~70,000 años (Estimado) | Imposible de terminar en la práctica por la cantidad de operaciones. |

## Conclusiones

* **El impacto de imprimir en pantalla vs. calcular en memoria:** En las pruebas se nota muchísimo cómo afecta dibujar en la consola. Con **5 discos** tardó **0.39 segundos**, pero fue únicamente porque tenía activado el modo visual para ver cómo se movían los discos entre los postes A, B y C. En cambio, al probar con **10 discos** (donde el modo visual se apaga automáticamente), el procesador hizo los 1,023 movimientos en apenas **0.000124 segundos**. Esto demuestra que para la computadora lo tardado no es hacer el cálculo recursivo, sino imprimir el texto en pantalla y esperar las pausas.
* **Crecimiento exponencial ($2^n - 1$):** El tiempo necesario no sube de forma normal (lineal), sino que se duplica por cada disco nuevo que agregamos. Con 10 discos es casi instantáneo, pero al subir a **30 discos** los movimientos pasan de mil a más de **1,073 millones**. Si tomamos como referencia lo que tardó mi computadora con 10 discos, resolver 30 discos en modo rápido tomaría alrededor de **133 segundos (un poco más de 2 minutos)** trabajando al 100% solo moviendo datos en las listas.
* **El límite con los 64 discos:** Aunque el código está bien hecho y en teoría puede resolver cualquier número, con **64 discos** la fórmula da más de **18.4 trillones de movimientos**. Haciendo el cálculo con la misma velocidad que me dio en la prueba de 10 discos, el programa tardaría aproximadamente **70,000 años** en terminar (e incluso teniendo el procesador más rápido, tomaría miles de años). Es un buen ejemplo de cómo un algoritmo tan corto puede superar por completo la capacidad física de cualquier computadora actual cuando el crecimiento es exponencial.
