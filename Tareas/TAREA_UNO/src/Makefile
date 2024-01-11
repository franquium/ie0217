# Nombres de archivos
SOURCE_FILES := main.cpp funciones.cpp
EXECUTABLE := salida.exe # Nota para Linux la extension del ejecutable es indiferente

# Comando de eliminacion
ifeq ($(OS),Windows_NT)
    RM = del /Q
    FixPath = $(subst /,\,$1) # Para cambiar Rutas en WN
else
    RM = rm -f
    FixPath = $1
endif

# Reglas
.PHONY: all build run clean

# Regla principal
all: build run

# Regla para construir el programa
build:
	g++ -o $(EXECUTABLE) $(SOURCE_FILES)

# Regla para ejecutar el programa
run:	
	./$(call FixPath,$(EXECUTABLE))

# Regla para limpiar de los archivos compilados el directorio 
# NOTA: No logro que elimine el ejecutable y no se el porque :(
clean:
	ifeq ($(OS),Windows_NT)
		del $(EXECUTABLE).exe 
	else
		rm -f $(EXECUTABLE).exe
	endif
