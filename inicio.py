import pandas as pd

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
