# Nota dado a que no se tienen los archivos a manipular, los codigos no van a correr sin error
# sin embargo, se copian los codigos para el estudio de la sintaxis

# Para abrir un archivo en el mismo dir
file1 = open("test.txt")

file1 = open("test.txt", "r")

file1 = open("test.txt", "w") # en modo escribir o write

file1 = open("test.txt", "r+b") # modos binarios de leer y escribir


# abrir un archivo
file1 = open("test.txt", "r")

# leer un archivo
read_content = file1.read()
print(read_content)

# cerrar un archivo
file1.close()


with open("test.txt", "r") as file1:
    read_content = file1.read()
    print(read_content)


# ejm
    
try:
    file1 = open("test.txt", "r")
    read_content = file1.read()
    print(read_content)
finally:
    # close the file
    file1.close()

with open('test2.txt', 'w') as file2:
    # write contents to the test2.txt file
    file2.write('Programming is Fun.')

# Ejemplos de Manejo de archivos: Directorios

# Ejm 1
import os

print(os.getcwd()) # Salida: C:\Program Files\PyScripter

# Ejm 2
import os

# cambiar dir
os.chdir('C:\\Python33')

print(os.getcwd())  # Salida: C:\Python33

# Ejm 3
import os

# borrar dir vacio "mydir"
os.rmdir("mydir")

# Ejm 4
import os

print(os.getcwd())
# C:\Python33

# list all sub-directories
os.listdir()
['DLLs',
 'Doc',
 'include',
 'Lib',
 'libs',
 'LICENSE.txt'
 'NEWs.txt'
 ]

os.listdir('G:\\')
['$RECYCLE.BIN', 
 'Movies',
 'Music',
 'Photos',
 'Series',
 'System Volume Information']

# Ejm 5

os.mkdir('test')

os.listdir()
# ['test']

# Ejm 6

import os

os.listdir()
# ['test']

# renombrando un dir
os.rename('test', 'new_one')

os.listdir()
['new_one']


