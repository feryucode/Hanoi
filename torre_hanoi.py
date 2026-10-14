import time
import os
import sys


DISCOS = 30


RETRASO = 0  
MODO_VISUAL = DISCOS <= 6  

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_torres(torres, num_discos):
    limpiar_pantalla()
    print(f"--- RESOLVIENDO TORRE DE HANOI CON {num_discos} DISCOS ---\n")
    
    for nivel in range(num_discos - 1, -1, -1):
        fila = ""
        for poste in ['A', 'B', 'C']:
            if nivel < len(torres[poste]):
                tamaño_disco = torres[poste][nivel]
                disco_dibujado = "*" * (tamaño_disco * 2)
            else:
                disco_dibujado = "|"
            
            ancho_columna = num_discos * 2 + 2
            fila += disco_dibujado.center(ancho_columna)
        print(fila)
    
    ancho_columna = num_discos * 2 + 2
    print("-" * (ancho_columna * 3))
    print("A".center(ancho_columna) + "B".center(ancho_columna) + "C".center(ancho_columna))
    print("\n")
    time.sleep(RETRASO)

def mover_disco(torres, origen, destino, num_discos):
    disco = torres[origen].pop()
    torres[destino].append(disco)
    if MODO_VISUAL:
        imprimir_torres(torres, num_discos)

def hanoi_animado(n, origen, auxiliar, destino, torres, num_discos):
    if n == 1:
        mover_disco(torres, origen, destino, num_discos)
        return
    
    hanoi_animado(n - 1, origen, destino, auxiliar, torres, num_discos)
    mover_disco(torres, origen, destino, num_discos)
    hanoi_animado(n - 1, auxiliar, origen, destino, torres, num_discos)

if __name__ == "__main__":
    if DISCOS >= 64:
        print("Advertencia: 64 discos requieren 18.4 trillones de movimientos (tardaría miles de años).")
        sys.exit()

    estado_torres = {
        'A': list(range(DISCOS, 0, -1)),
        'B': [],
        'C': []
    }

    if MODO_VISUAL:
        imprimir_torres(estado_torres, DISCOS)
        time.sleep(1)
    else:
        print(f"Calculando {DISCOS} discos en modo rápido (sin animación para no tardar años)...")

    inicio = time.perf_counter()
    hanoi_animado(DISCOS, 'A', 'B', 'C', estado_torres, DISCOS)
    fin = time.perf_counter()
    
    tiempo_total = fin - inicio
    movimientos = (2 ** DISCOS) - 1
    
    print(f"¡Terminado!")
    print(f"Total de discos: {DISCOS}")
    print(f"Movimientos realizados: {movimientos:,}")
    print(f"Tiempo de ejecución: {tiempo_total:.6f} segundos")