# Importamos el módulo de aleatoriedad
import random

# Estas son las frecuencias obtenidas, que son cero para todos los
# posibles resultados al principio
frequencies = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

# Estas son las frecuencias esperadas por la teoría de probabilidad
probabilities = {2:2.78, 3:5.56, 4:8.33, 5:11.11, 6:13.89, 7:16.67,
                 8:13.89, 9:11.11, 10:8.33, 11:5.56, 12:2.78}

# Cuantas veces hacemos el experimento
TOTAL_ROLLS = 1000

def roll():
    '''Esta función simplemente simula el lanzamiento del dado una
    vez y suma 1 al resultado que ha salido. El diccionario es una
    variable global, para que pueda guardar los resultados cada
    vez que la función se ejecuta
    '''
    global frequencies
    result = random.randint(1,6) + random.randint(1,6)
    frequencies[result] += 1

# Jugamos....
for i in range(TOTAL_ROLLS):
    roll()

# Imprimimos la primera línea
print("Suma\tSimulado\tEsperado")
# Ahora imprimimos las frecuencias obtenidas y ls esperadas
# Está en porcentajes, con los cual hay que multiplicar la
# frecuencia obtenida por 100 y dividir por el número de
# veces que lanzamos el dado
for i in frequencies:
    print(i, "\t", frequencies[i]*100.0/TOTAL_ROLLS, "\t\t", probabilities[i])
