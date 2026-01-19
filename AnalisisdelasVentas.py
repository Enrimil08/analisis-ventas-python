import pandas as pd
import matplotlib.pyplot as plt

def analizar_ventas(archivo_csv):
    """
    Realiza un análisis básico de un archivo CSV de ventas.
    """
    try:
        # 1. Cargar los datos
        df = pd.read_csv(archivo_csv)
        print(f"Datos cargados exitosamente desde {archivo_csv}\n")
        print("Primeras 5 filas del dataset:")
        print(df.head())
        print("\nInformación general del dataset:")
        df.info()

        # 2. Calcular el total de ventas por fila
        df['TotalVenta'] = df['Cantidad'] * df['PrecioUnitario']

        # 3. Métricas clave
        total_ingresos = df['TotalVenta'].sum()
        productos_unicos = df['Producto'].nunique()
        ventas_por_region = df.groupby('Region')['TotalVenta'].sum().sort_values(ascending=False)
        productos_mas_vendidos = df.groupby('Producto')['Cantidad'].sum().sort_values(ascending=False).head(3)

        print(f"\n--- Resumen del Análisis ---")
        print(f"Ingresos Totales: ${total_ingresos:,.2f}")
        print(f"Número de Productos Únicos: {productos_unicos}")
        print(f"\nVentas por Región:")
        print(ventas_por_region)
        print(f"\nTop 3 Productos Más Vendidos (por cantidad):")
        print(productos_mas_vendidos)

        # 4. Generar un gráfico de barras de ventas por región
        plt.figure(figsize=(10, 6))
        ventas_por_region.plot(kind='bar', color='skyblue')
        plt.title('Ingresos Totales por Región')
        plt.xlabel('Región')
        plt.ylabel('Ingresos Totales ($)')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig('ingresos_por_region.png') # Guarda el gráfico como imagen
        print("\nGráfico 'ingresos_por_region.png' generado exitosamente.")
        # plt.show() # Descomenta esta línea si quieres ver el gráfico inmediatamente
        
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_csv}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error durante el análisis: {e}")

import os

if __name__ == "__main__":
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(directorio_actual, 'Ventas.csv')
    
    analizar_ventas(ruta_archivo)