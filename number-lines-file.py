import sys
NUM_LINES=10
if len(sys.argv) != 3:
   print("Missing file(s) name")
   quit()

try:
    fd = open(sys.argv[1], "r")
except FileNotFoundError:
    print("File does not exist")
else:
    fdd = open(sys.argv[2], "w")
    line = fd.readline()
    count = 1
    while line != "":
#        line = line.rstrip()
        count += 1
        fdd.write("%d: " % count)
        fdd.write(line)
        line = fd.readline()
    fd.close()
    fdd.close()
