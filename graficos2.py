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

# Analizar usuarios con mayor consumo de minutos fuera del país
if 'Minutos Main Out Peru soles' in min_megas_soles_df:
    minutos_out_peru_df = min_megas_soles_df['Minutos Main Out Peru soles']
    
    # Relacionar las tablas usando la columna 'DNI'
    minutos_out_peru_df = minutos_out_peru_df.merge(clientes_df[['DNI', 'Cliente']], on='DNI')
    
    # Usuarios con mayor consumo de minutos fuera del país
    top_users = minutos_out_peru_df.groupby(['Cliente'])['Min Out Perú'].sum().nlargest(10)
    top_users.plot(kind='bar')
    plt.title('Usuarios con Mayor Consumo de Minutos fuera del País')
    plt.xlabel('Cliente')
    plt.ylabel('Minutos')
    plt.show()
    
    # Consumo promedio en soles de los usuarios fuera del país
    avg_consumo_soles = minutos_out_peru_df.groupby(['Cliente'])['Minutos Soles'].mean().nlargest(10)
    avg_consumo_soles.plot(kind='bar')
    plt.title('Consumo Promedio en Soles de Usuarios fuera del País')
    plt.xlabel('Cliente')
    plt.ylabel('Soles Promedio')
    plt.show()
