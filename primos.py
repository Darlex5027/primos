import time
import math

def es_primo(n):
    """Verifica si un número es primo."""
    contador = 0
    for i in range(1, n + 1):
        if n % i == 0:
            contador += 1
    return contador == 2

def contar_primos(m):
    """Cuenta la cantidad de números primos hasta m."""
    contador = 0
    for j in range(2, m + 1):
        if es_primo(j):
            contador += 1
    return contador

def main():
    """Función principal que calcula y muestra el número de primos y el tiempo."""
    k = 2**0
    print("{:<20} {:<20} {:<20}".format("N", "S", "TIEMPO"))  # Formateo de la salida
    p = k
    while p <= 131072:
        print("{:<20}".format(p), end="") #Imprimo el valor de p
        tiempo_invertido = 0.0
        inicio = time.time()
        num_primos = contar_primos(p)
        fin = time.time()
        tiempo_invertido += fin - inicio
        print("{:<20} {:<20}".format(num_primos, tiempo_invertido)) #imprimo la cantidad de primos y el tiempo
        p *= 2

if __name__ == "__main__":
    main()