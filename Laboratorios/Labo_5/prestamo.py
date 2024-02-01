import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  


class Prestamo:
    
    # constructor de la clase
    def __init__(self, monto_prestamo, tasa_interes_anual, cuotas):
        self.monto_prestamo = monto_prestamo
        self.tasa_interes_anual = tasa_interes_anual
        self.cuotas = cuotas
        self.amortizacion = self.calcular_amortizacion()

    # Definiendo metodo para calcular amortizacion
    def calcular_amortizacion(self):
        try:
            tasa_interes_mensual = self.tasa_interes_anual / 12 / 100
            cuota_mensual = (tasa_interes_mensual * self.monto_prestamo) / (1 - (1 + tasa_interes_mensual)**-self.cuotas)

            saldo_restante = self.monto_prestamo
            amortizacion = []

            for cuota in range(1, self.cuotas + 1):
                interes_pendiente = saldo_restante * tasa_interes_mensual
                amortizacion_principal = cuota_mensual - interes_pendiente

                saldo_restante -= amortizacion_principal
<<<<<<< HEAD
                amortizacion.append({'Cuota': cuota, 
                                     'Interes': interes_pendiente, 
                                     'Amortizacion': amortizacion_principal, 
                                     'Saldo Restante': saldo_restante})
=======
                amortizacion.append({'Cuota': cuota, 'Interes': interes_pendiente, 'Amortizacion': amortizacion_principal, 'Saldo Restante': saldo_restante})
>>>>>>> e531dbacb7f0ba85ecd550c98ee6bed9b2a49bfd
            return amortizacion
        
        except ZeroDivisionError:
            print("Error: La cantidad de cuotas no puede ser cero")
            return []   # Lista vacia
        
    # Metodo para generar reporte
    def generar_reporte(self, archivo_salida):
        try:
            df = pd.DataFrame(self.amortizacion)
            df.to_csv(archivo_salida, index=False)
            print(f'Reporte generado con exito: {archivo_salida}')
        except Exception as e:
            print(f'Ocrurrio un error al generar el reporte: {str(e)}')

    # Metodo para graficar
    def graficar_amortizacion(self):
        df = pd.DataFrame(self.amortizacion)

        data = np.array([df['Interes'], df['Amortizacion']])

        plt.bar(df['Cuota'], data[0], label='Interes')
        plt.bar(df['Cuota'], data[1], bottom=data[0], label='Amortizacion')

        plt.xlabel('Numero de cuota')
        plt.ylabel('Monto ($)')
        plt.title('Amortizacion e Interes por Cuota')
        plt.legend()
        plt.show()


def main():
    print("Hola")
    """ 
    Lista de cosas a hacer
    1. perdir el monto al usuario
    2. pedir la tasa de interes anual (%)
    3. pedir la cantidad de cuotas
    4. Instanciar el prestamo
    5. Generar el reporte
    6. Imprimir info: monto, tasa, cuotas
    7. Graficar la amortizacion
    8. Manejo de Excepciones: ValueError y generico
    """

    try:
        # 1 Perdir el monto al usuario
        monto = float(input("Ingrese el monto del prestamo: "))
        if monto < 0:
            raise ValueError

        # 2 pedir la tasa de interes anual (%)
        tasa_interes = float(input("Ingrese la tasa de interes: "))
        if tasa_interes < 0:
            raise ValueError

        # 3 pedir la cantidad de cuotas
        cuotas = int(input("Ingrese la cantidad de cuotas: "))
        if cuotas <= 0:
            raise ValueError

        # 4 Instanciar el prestamo
        prestamo = Prestamo(monto, tasa_interes, cuotas)

        # 5 Generar el reporte
        nombre_archivo = "reporte_prestamo.csv"
        prestamo.generar_reporte(nombre_archivo)

        # 6 Imprimir info: monto, tasa, cuotas
        print(f"Monto del prestamo: {monto}")
        print(f"Tasa de interes anual: {tasa_interes} %")
        print(f"Cantidad de cuotas: {cuotas}")

        # 7 Graficar la amortizacion
        prestamo.graficar_amortizacion()

    # 8 Manejo de Excepciones: ValueError y generico
    except ValueError:
        print("Error en el valor: El valor no puede ser negativo.")

    except Exception as e:
        print(f"Ocurrio un error: {e}")

    except Exception as e:
        print(f"Ocurrio un error: {e}")


if __name__ == "__main__":
    main()
