import time
import random

def insertar_intervalos(cantidad):
    elementos = [
        max(1, cantidad // 4),
        max(1, cantidad // 2),
        cantidad
    ]
    return sorted(set(elementos))

def generar_numeros(cantidad):
    inicio = time.perf_counter()
    datos = [random.randint(0, 5_000_000) for _ in range(cantidad)]
    fin = time.perf_counter()
    tiempo = fin - inicio
    return datos, tiempo

def ordenar_burbuja(datos):
    inicio = time.perf_counter()
    n = len(datos)
    for i in range(n - 1):
        intercambio = False
        for j in range(n - 1 - i):
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
                intercambio = True
        if not intercambio:
            break
    fin = time.perf_counter()
    tiempo = fin - inicio
    return datos, tiempo

cantidad = int(input("cantidad de elementos: "))
datos, tiempo = generar_numeros(cantidad)
print(f"\nTiempo de generación: {tiempo:.4f} s")
print("\nfin de generación")
ini = time.perf_counter()
print(datos)
fin = time.perf_counter()
dif = fin - ini
print(f"\nDuración de impresión: {dif:.4f} s")
datos, tiempo_orden = ordenar_burbuja(datos)
print("\nfin de ordenamiento")
ini = time.perf_counter()
print(datos)
fin = time.perf_counter()
dif = fin - ini
print(f"\nTiempo de ordenamiento: {tiempo_orden:.4f} s")
print(f"Duración de impresión (ordenado): {dif:.4f} s")