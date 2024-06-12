import pandas as pd
import matplotlib.pyplot as plt

# Verificar archivos en el directorio actual
import os
print("Archivos en el directorio actual:")
for file in os.listdir('.'):
    print(file)

# Leer los archivos Excel
clientes_df = pd.read_excel('BD Clientes.xlsx')
op_min_megas_df = pd.read_excel('BD Min,Megas x Dia Sem.xlsx')
min_megas_soles_df = pd.read_excel('BD Min,Megas Soles IN & OUT Peru.xlsx', sheet_name=None)  # Leer todas las hojas

# Mostrar primeras filas de cada DataFrame para verificar la carga correcta
print("Clientes DataFrame:")
print(clientes_df.head())

print("\nOP Min Megas DataFrame:")
print(op_min_megas_df.head())

print("\nMin Megas Soles DataFrames:")
for sheet_name, df in min_megas_soles_df.items():
    print(f"\nSheet: {sheet_name}")
    print(df.head())

# Distribución de edades en el archivo de clientes
if 'Edad' in clientes_df.columns:
    clientes_df['Edad'].plot(kind='hist', bins=20, edgecolor='black')
    plt.title('Distribución de Edades')
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')
    plt.show()

# Consumo de Megas Web por día de la semana
if 'Dia Sem' in op_min_megas_df.columns and 'Megas Web' in op_min_megas_df.columns:
    op_min_megas_df.groupby('Dia Sem')['Megas Web'].sum().plot(kind='bar')
    plt.title('Consumo de Megas Web por Día de la Semana')
    plt.xlabel('Día de la Semana')
    plt.ylabel('Megas Web')
    plt.show()

# Consumo de Soles en Megas Web por mes en el libro "Mega Web (Soles)"
if 'Megas Web (Soles)' in min_megas_soles_df:
    mega_web_soles_df = min_megas_soles_df['Megas Web (Soles)']
    mega_web_soles_df.set_index('DNI', inplace=True)
    mega_web_soles_df.sum().plot(kind='bar')
    plt.title('Consumo de Soles en Megas Web por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Soles')
    plt.show()

# Consumo de Soles en Minutos IN Perú por mes en el libro "Minutos Perú Soles"
if 'Minutos Peru Soles' in min_megas_soles_df:
    minutos_peru_soles_df = min_megas_soles_df['Minutos Peru Soles']
    minutos_peru_soles_df.set_index('DNI', inplace=True)
    minutos_peru_soles_df.sum().plot(kind='bar')
    plt.title('Consumo de Soles en Minutos IN Perú por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Soles')
    plt.show()

# Consumo de Minutos OUT Perú por país en el libro "Minutos Main Out Peru soles"
if 'Minutos Main Out Peru soles' in min_megas_soles_df:
    minutos_out_peru_df = min_megas_soles_df['Minutos Main Out Peru soles']
    if 'Pais' in minutos_out_peru_df.columns and 'Min Out Perú' in minutos_out_peru_df.columns:
        minutos_out_peru_df.groupby('Pais')['Min Out Perú'].sum().plot(kind='bar')
        plt.title('Consumo de Minutos OUT Perú por País')
        plt.xlabel('País')
        plt.ylabel('Minutos')
        plt.show()
