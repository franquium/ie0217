# Nombres de archivos
SOURCE_FILE1 := ./cars_analysis/main.py

# Reglas
.PHONY: all 

# Regla principal
all: run 

# Regla para construir y correr el programa en linux
ifeq ($(OS),Linux)
run:
	python3 $(SOURCE_FILE1)
		
endif

# Regla para construir y correr el programa en linux
ifeq ($(OS),Windows_NT)
run:
	python $(SOURCE_FILE1)

		
endif


