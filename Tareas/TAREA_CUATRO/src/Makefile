# Nombres de archivos
SOURCE_FILES := main.py 


# Reglas
.PHONY: all 

# Regla principal
all: build 

# Regla para construir y correr el programa en linux
ifeq ($(OS),Linux)
build:
	python3 $(SOURCE_FILES)
		
endif

# Regla para construir y correr el programa en linux
ifeq ($(OS),Windows_NT)
build:
	python $(SOURCE_FILES)
		
endif

