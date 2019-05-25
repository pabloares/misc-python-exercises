# Encuentra la(s) palabra(s) más largas en un fichero.
# El nombre del fichero está en el código, pero se
# podría preguntar al usuario.
# La longitud de la palabra más larga, empezamos con cero
longest = 0
# La lista de las palabras más largas, empieza vacía
lista = []

def listlong(string):
   '''Esta función lee una cadena, la divide en palabras,
   separadas por espacios, y compara la longitud de cada
   palabra con la longitud de la palabra más larga (de momento).
   Si la palabra nueva es más larga, ponemos su longitud como
   la longitud más larga, vaciamos la lista, y ponemos la palabra
   en la lista. Si la palabra nueva es igual de larga que la máxima,
   añadimos la palabra a la lista. En cualquier otro caso no hacemos
   nada.
   Las variables "longest" y "lista" deben ser globales, para que
   no se borren cada vez que la función se ejecuta, por eso tiene
   "global"
   '''
   global longest
   global lista
   splitstring = string.split()
   for word in splitstring:
      if len(word) > longest:
         longest = len(word)
         lista = []
         lista.append(word)
      elif len(word) == longest:
         lista.append(word)
   return

# Abrimos el archivo
try:
   fd = open('/etc/services', "r")
   # Error si el archivo no existe en la carpeta donde
   # estamos ejecutando el programa, o en la carpeta
   # dada.
except FileNotFoundError:
   print("File does not exist")
   quit()
# El código en caso que se pueda abrir el archivo
else:
   # Leemos línea a línea
   for line in fd:
   # Ejecutamos la función que nos encuentra las palabras más largas
   # Por eso necesitamos variables globales
      listlong(line)
   # Cerramos el archivo
   fd.close()

# Imprimimos la longitud y la lista
print("The longest word has", longest, "characters")
print("The list of longest words is the following:")
print(lista)
