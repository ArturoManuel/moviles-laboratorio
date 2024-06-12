import pandas as pd
import matplotlib.pyplot as plt

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

# Análisis de estacionalidad por mes
op_min_megas_df['Mes 2018'] = pd.Categorical(op_min_megas_df['Mes 2018'], 
                                             categories=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'], 
                                             ordered=True)
consumo_mensual = op_min_megas_df.groupby('Mes 2018')[['Minutos', 'Megas Web', 'Megas Whatsapp', 'Megas Facebook']].sum()

# Gráfico de líneas para consumo mensual
consumo_mensual.plot(kind='line', marker='o')
plt.title('Consumo Mensual de Minutos y Megas')
plt.xlabel('Mes')
plt.ylabel('Consumo')
plt.legend(['Minutos', 'Megas Web', 'Megas Whatsapp', 'Megas Facebook'])
plt.grid(True)
plt.show()

# Análisis de estacionalidad por día de la semana
op_min_megas_df['Dia Sem'] = pd.Categorical(op_min_megas_df['Dia Sem'], 
                                            categories=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'], 
                                            ordered=True)
consumo_diario = op_min_megas_df.groupby('Dia Sem')[['Minutos', 'Megas Web', 'Megas Whatsapp', 'Megas Facebook']].sum()

# Gráfico de líneas para consumo diario
consumo_diario.plot(kind='line', marker='o')
plt.title('Consumo Diario de Minutos y Megas')
plt.xlabel('Día de la Semana')
plt.ylabel('Consumo')
plt.legend(['Minutos', 'Megas Web', 'Megas Whatsapp', 'Megas Facebook'])
plt.grid(True)
plt.show()

# Gráfico de barras apiladas para consumo mensual de diferentes tipos de datos
consumo_mensual[['Megas Web', 'Megas Whatsapp', 'Megas Facebook']].plot(kind='bar', stacked=True)
plt.title('Consumo Mensual de Diferentes Tipos de Megas')
plt.xlabel('Mes')
plt.ylabel('Megas')
plt.legend(['Megas Web', 'Megas Whatsapp', 'Megas Facebook'])
plt.grid(True)
plt.show()
