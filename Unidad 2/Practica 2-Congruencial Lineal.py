# Simulación
# Unidad 2
# Práctica 2. Generación de numeros pseudoaleatorios por el método de medios al cuadrado
# Profesor: José Gabriel Rodríguez Rivas
# Alumno: Romero Rodríguez Leonardo Antonio

def metodo_congruencial_lineal(x0, a, c, m, n):
    # Genera n números pseudoaleatorios usando el método congruencial lineal.
    numeros = []
    xn = x0  # Semilla inicial
    for _ in range(n):
        xn = (a * xn + c) % m  # Fórmula del método congruencial lineal
        numeros.append(xn)
    return numeros

# Parámetros
x0 = 2005   # Semilla
a = 11    # Multiplicador
c = 3    # Incremento
m = 200   # Módulo
n = 100   # Cantidad de números generados

# Generar números pseudoaleatorios
numeros_pseudoaleatorios = metodo_congruencial_lineal(x0, a, c, m, n)
print(numeros_pseudoaleatorios)
