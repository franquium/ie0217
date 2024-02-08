# Nombres de archivos
SOURCE_FILE1 := trafico_aereo.py
SOURCE_FILE2 := calificaciones_estudiantes.py


# Reglas
.PHONY: all 

# Regla principal
all: run1 run2

# Regla para construir y correr el programa en linux
ifeq ($(OS),Linux)
run1:
	python3 $(SOURCE_FILE1)
	
run2:
	python3 $(SOURCE_FILE2)
		
endif

# Regla para construir y correr el programa en linux
ifeq ($(OS),Windows_NT)
run1:
	python $(SOURCE_FILE1)

run2:
	python $(SOURCE_FILE2)
		
endif


