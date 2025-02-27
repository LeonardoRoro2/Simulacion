# Simulación
# Unidad 2
# Práctica 1. Generación de numeros pseudoaleatorios por el método de medios al cuadrado
# Profesor: José Gabriel Rodríguez Rivas
# Alumno: Romero Rodríguez Leonardo Antonio

# Se eleva al cuadrado la semilla, se calcula la nueva semilla y se devuelve el nuevo valor de la semilla
def Calcular_Semilla_MC(semilla, n_digitos):
    # Elevar la semilla al cuadrado
    cuadrado = str(semilla ** 2).zfill(2*n_digitos) # Agregar los espacios necesarios
    # Extraer los digitos centrales
    centro = cuadrado[len(cuadrado)//2 - n_digitos//2 : len(cuadrado)//2 + n_digitos//2]
    return int(centro)
    
# Se realiza el producto de las dos semillas, se calculan la nueva semilla y se devuelven los nuevos valores de las semillas
def Calcular_Semilla_CC(semilla, semilla2, n_digitos):
    # Realizar el producto de las dos semillas
    producto = str(semilla * semilla2).zfill(2*n_digitos) # Agregar los espacios necesarios
    # Extraer los digitos centrales
    centro = producto[len(producto)//2 - n_digitos//2 : len(producto)//2 + n_digitos//2]
    return semilla2, int(centro)
    
# Numeros aleatorios calculados por el método de medios al cuadrado
def medios_al_cuadrado(semilla,n_digitos,iteraciones):
    resultados = []
    for _ in range(iteraciones):
        semilla = Calcular_Semilla_MC(semilla, n_digitos)
        resultados.append(semilla)
    return resultados
# Numeros aleatorios calculados por el método de centros al cuadrado
def centros_al_cuadrado(semilla,semilla2,n_digitos,iteraciones):
    resultados = []
    for _ in range(iteraciones):
        semilla, semilla2 = Calcular_Semilla_CC(semilla,semilla2, n_digitos)
        resultados.append(semilla2)
    return resultados

# Semilla Inicial
semilla = 2111
n_digitos = 4
#semilla2 = Calcular_Semilla_MC(semilla, n_digitos)
semilla2 = 1999
iteraciones = 100

# Imprimir los resultados
# Medios al cuadrado
print("Numeros aleatorios calculados por el método de medios al cuadrado")
for i, numero in enumerate(medios_al_cuadrado(semilla,n_digitos,iteraciones), 1):
  print(f"Numero Aleatorio {i}: {numero}")
print("")
# Centros al cuadrado
print("Numeros aleatorios calculados por el método de centros al cuadrado")
for i, numero in enumerate(centros_al_cuadrado(semilla,semilla2,n_digitos,iteraciones), 1):
  print(f"Numero Aleatorio {i}: {numero}")
