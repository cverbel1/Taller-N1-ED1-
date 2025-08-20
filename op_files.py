class F:
    def read(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            for linea in f: 
                print(linea.strip())


    def write(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Encabezado\n")
            f.writelines(["linea 1\n", "linea 2\n"])


f = F()
f.read("notes.txt")
f.write("notes.txt")            