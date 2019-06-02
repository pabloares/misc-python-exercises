# Intentamos abrir el fichero
try:
    fd = open("IBM.csv", "r")

# Error si no existe
except FileNotFoundError:
    print("El fichero no existe")

# El programa. Primero leemos las lineas del fichero,
# quitando el ultimo caracter (\n) y las comas
# 
else:
    lines = [line.rstrip().split(',') for line  in fd]
    fd.close()

# Abrimos el fichero donde vamos a guardar el resultado
    fd = open("IBM.vsc", "w")

# Esto es como transponer una matriz, i es para las columnas
# (estamos suponiendo todas tienen el mismo numero de datos)
# y j para las filas, que es el numero de listas en la variable lines
# Escribimos todas las columnas menos la ultima, pq no queremos
# una coma al final. Luego escribimos el ultio dato y nueva line (\n)
    for i in range(len(lines[0])):
        for j in range(len(lines)-1):
            fd.write(lines[j][i])
            fd.write(',')
        fd.write(lines[j][len(lines[0])-1])
        fd.write('\n')

# Somos buenos y cerramos el fichero
    fd.close()
          
    

