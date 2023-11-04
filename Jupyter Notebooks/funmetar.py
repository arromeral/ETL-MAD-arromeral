import numpy as np
import pylab as plt   
import seaborn as sns
import pandas as pd
import re
def check_nan(df: pd.DataFrame) -> None:
    
    """
    Recibe un dataframe y enseña el % de valores nulos
    y lo grafica
    """
    
    nan_cols = df.isna().mean() * 100  # porcentaje de nulo en cada columna
    
    display(f'N nan cols: {len(nan_cols[nan_cols>0])}')
    display(nan_cols[nan_cols>0])
    
    
    # grafico de nulos en el dataframe
    #inicializa figura y establece un tamaño
    plt.figure(figsize=(100, 60)) # 100x60 pixeles

    sns.heatmap(df.isna(),          # datos
                yticklabels=False,  # quita las etiquetas del eje y
                cmap='viridis',     # mapa de color
                cbar=False,         # sin barra lateral
               )

    plt.show();

def generar_columna_gust(valor):
    pattern = re.compile(r'^(\d{2})\s')  # Dos dígitos seguidos de un espacio
    match = pattern.match(valor)


    if match:
        return match.group(1)

    else:
        return 0

def fix_hum_column(row):
    if row['Relative_hum'].strip() == '>':
        match = re.search(r'(\w{2})%', row['Pressure'])
        
        if match:
            return match.group(1)
        else:
            return row['Relative_hum']
    else:
        return row['Relative_hum']

