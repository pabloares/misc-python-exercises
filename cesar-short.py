string = input("Introduce una frase: ")
shift = int(input("Numero entre 1 y 25 para cifrar: "))
newstring = ""
for i in string:
    n = ord(i)
    if n >= 65 and n <= 90:
        newstring += chr(((n-65+shift) % 26) + 65)
    elif n >= 97 and n <= 122:
        newstring += chr(((n-97+shift) % 26) + 97)
    else:
        newstring += i
print(newstring)
