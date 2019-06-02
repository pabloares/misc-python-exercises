# Maximum
def maxval(file):
    '''Esta funcion calcula el valor maximo de unos datos
    en un fichero. Utiliza la funcion max de python y
    supone que los datos no son negativos, por eso inicializa
    el maximo en cero
    '''
# Abrimos el fichero
    filename = file + ".txt"
    fd = open(filename, "r")
# Inicializamos el maximo a cero, pq los valores no son negativos.
# Si el fichero tuviera valores negativos esto no se puede hacer
# Abria que coger los dos primeros valores y calcular el maximo
    maximum = 0.0
    data = fd.readlines()
    fd.close()
    for number in data:
        n = float(number)
        maximum = max(maximum, n)
    return maximum

# Minimum
def minval(file):
    '''Esta funcion calcula el valor maximo de unos datos
    en un fichero. Utiliza la funcion min de python
    '''
# Abrimos el fichero
    filename = file + ".txt"
    fd = open(filename, "r")
# Inicializamos el minimo como el valor maximo del fichero
# utilizando la funcion anterior
    minimum = maxval(file)
    data = fd.readlines()
    fd.close()
    for number in data:
        n = float(number)
        minimum = min(minimum, n)
    return minimum

# Average
def mean(file):
    '''Esta funcion calcula la media de unos datos en un fichero.
    '''
# Abrimos el ficheroo
    filename = file + ".txt"
    fd = open(filename, "r")
# La suma empieza en cero pq empezamos sin valores. Si no hubiera
# valores deberia devolver un error, pero si no hay valoress no
# tiene sentido calcular todo esto
    sum = 0.0
    count = 0
# Leemos todos los datos en una lista
    data = fd.readlines()
    fd.close()
# Sumamos los datos de la lista, convirtiendolos a numeros
# y al mismo tiempo contamos cuantos datos tenemos
    for number in data:
        sum += float(number)
        count += 1
# Calculamos la media. Aqui se podria introducir un control de
# errores, pues si no hay datos, count=0 y no se puede dividir por 0
    return (sum / count)

# Los tres estadisticos
def stats(what, file):
    '''Esta funcion calcula el estadistico pedido de los
    datos en el fichero correspondiente. Imprime el resultado
    y lo devuelve tambien para calculos futuros
    '''
    if what == "max":
        print("The maximum value is ", maxval(file))
        return maxval(file)
    elif what == "min":
        print("The minimum value is ", minval(file))
        return minval(file)
    elif what == "mean":
        print("The average is ", mean(file))
        return mean(file)
    else:
        print("estadistico no existe")

# Aqui empieza el programa
# Abrimos el csv para leer y los demas vacios para escribir
fd = open("IBM.csv", "r")
fd1 = open("dates.txt", "w")
fd2 = open("open.txt", "w")
fd3 = open("high.txt", "w")
fd4 = open("low.txt", "w")
fd5 = open("close.txt", "w")
fd6 = open("adjclose.txt", "w")
fd7 = open("volume.txt", "w")

# Esta line contiene los nombres de las variables, no la queremos
# Es la primera linea del csv
line = fd.readline()
# Leemos una line de nuevo para evitar la primera linea con los
# nombres. Los nombres se entienden por el nombre del fichero
line = fd.readline()

# Leemos las lineas, que contienen los datos separados por
# comas, asi que los separamos en diversos valores y
# escribimos los datos en los diferentes ficheros
# Hay que añadir una nueva linea tras cada dato
# para que no sea algo que no se puede manejar, es
# decir un fichero con todos los datos juntos
while line:
    linelist = line.split(',')
    fd1.write(linelist[0])
    fd1.write('\n')
    fd2.write(linelist[1])
    fd2.write('\n')
    fd3.write(linelist[2])
    fd3.write('\n')
    fd4.write(linelist[3])
    fd4.write('\n')
    fd5.write(linelist[4])
    fd5.write('\n')
    fd6.write(linelist[5])
    fd6.write('\n')
    fd7.write(linelist[6])
# El ultimo dato contiene la parte de nueva linea, no
# hace falta añadir el caracter \n
    line = fd.readline()

# Somos niños buenos y cerramos todos los ficheros
fd.close()
fd1.close()
fd2.close()
fd3.close()
fd4.close()
fd5.close()
fd6.close()
fd7.close()

# Preguntamos que tipo de valores. Lo llamamos "thefile"
# simplemente porque el archivo se llama como los valores
thefile = input("open, high, low, close, adjclose, volume: ")

# Preguntamos que estadistico quiere
themeasure = input("max, min, mean: ")

# Llamamos a la funcion que imprime los estadisticos, con el
# estadistico que queremos, y guardamos el resultado para poder
# luego almacenar la fecha
result=stats(themeasure, thefile)

# Tenemos que leer el fichero con todos los datos, para poder
# encontrar donde esta el estadistico calculado
whatfile = thefile + ".txt"
fd = open(whatfile, "r")
thenumbers = fd.readlines()
fd.close()

# Leemos las fechas
fd1 = open("dates.txt", "r")
thedates = fd1.readlines()

# Esta cadena es simplemente para almacenar las fechas donde
# encontramos el estadistico
theresults = ""
# Comparamos los datos con el estadistico calculado. Si es
# igual, estamos en la posicion correcta, con lo cuall
# añadimos la fecha de esa posicion al resultado
for i in range(len(thenumbers)):
    if float(thenumbers[i]) == result:
         theresults += thedates[i]
         theresults += ","
# Imprimimos el resultado de fechas, comprobando antes que hay
# alguna fecha, lo cual ocurre si la longitud es mayor que 1
# Quitamos la ultima coma, que es muy fea. Para que fuera
# bonito habria que añadir un punto final, pero no me apetece :-)
if len(theresults) > 1:
    print("The value took place on", theresults[:-2])
