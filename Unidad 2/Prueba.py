import math

def factores_primos(n):
    """Devuelve los factores primos únicos de n"""
    factores = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factores.add(d)
            n //= d
        d += 1
    if n > 1:
        factores.add(n)
    return factores

def cumple_condicion_a(a, m):
    """Verifica si a - 1 es múltiplo de todos los factores primos de m"""
    factores_m = factores_primos(m)
    return all((a - 1) % p == 0 for p in factores_m)

# Ejemplo de prueba
m = 200
a = 11
c = 3
print(f"Factores primos de {m}: {factores_primos(m)}")
print(f"¿{a} cumple la condición? {cumple_condicion_a(a, m)}")

def son_primos_entre_si(a, b):
    return math.gcd(a, b) == 1

# Ejemplo
print(f"{m} y {c} son coprimos? {son_primos_entre_si(m, c)}")  # True (son coprimos)
