import time
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

def add_2023_if_needed(date):
    if not date.endswith('2022') and not date.endswith('2023'):
        return date + ' 2023'
    return date

def convertir_fecha(date):
    try:
        # Convierte el string de la fecha al formato de fecha reconocible por Pandas
        fecha = pd.to_datetime(date.strip(), format='%a, %d. %b %Y').strftime('%Y-%m-%d')
        return fecha
    except:
        return 'Formato incorrecto'  # Mensaje si hay un formato incorrecto

def separar_valores(dataframe, columna_origen):
    # Utilizar expresiones regulares para extraer los valores
    valores = dataframe[columna_origen].str.extract(r'^(?P<Valor_1>[A-Z0-9]+)/(?P<Valor_2>[A-Z0-9]+)')

    # Crear dos nuevas columnas con los valores extraídos
    dataframe['cod_airliner_IATA'] = valores['Valor_1']
    dataframe['cod_airliner_ICAO'] = valores['Valor_2']

def extraer_valores(dataframe, columna_origen):
    # Utilizar expresiones regulares para extraer los valores
    valores = dataframe[columna_origen].str.extract(r'[A-Z0-9]{2}/[A-Z0-9]{3}\s([A-Za-z\s\-]+)\s\(([A-Z]{3})\s/\s([A-Z]{4})\)')

    # Crear tres nuevas columnas con los valores extraídos
    dataframe['City'] = valores[0]
    dataframe['cod_airport_IATA'] = valores[1]
    dataframe['cod_airport_ICAO'] = valores[2]

def extraer_hora(dataframe, columna_origen):
    # Utilizar expresiones regulares para extraer la hora
    dataframe['Scheduled_dep'] = dataframe[columna_origen].str.extract(r'(\d{2}:\d{2})\s[A-Z0-9]')


def extraer_segunda_hora(dataframe, columna_origen):
    # Utilizar expresiones regulares para extraer la segunda hora
    dataframe['depart_time'] = dataframe[columna_origen].str.extract(r'\d{2}:\d{2}\s\w+\s(\d{2}:\d{2})\s\w+')

def redondear_horas(valor):
    if 'h' in valor and 'm' in valor:  # Verificar si el valor está en formato "Xh Xm"
        horas, minutos = map(int, re.findall(r'\d+', valor))  # Extraer horas y minutos
        if minutos >= 30:  # Redondear a la siguiente hora si los minutos son 30 o más
            horas += 1
        return f"{horas}h"
    elif 'm' in valor:  # En caso de formato "Xm", redondear siempre a 1h
        return "1h"
    else:
        return valor  # Mantener el valor original si es solo "Xh"

def asignar_estado_departure(celda):
    if 'scheduled' in celda:
        return 'on time'
    elif 'early' in celda:
        return 'early'
    elif 'late' in celda:
        return 'late'
    elif 'on time' in celda:
        return 'on time'
    else:
        return "-"

def calcular_minutos(celda):
    match = re.search(r'(\d+)h (\d+)min (late|early)', celda)
    if match:
        horas = int(match.group(1))
        minutos = int(match.group(2))
        valor = horas * 60 + minutos
        if match.group(3) == 'late':
            return valor
        else:
            return -valor
    elif 'min late' in celda or 'min early' in celda:
        minutos = int(re.search(r'(\d+)min (late|early)', celda).group(1))
        if 'late' in celda:
            return minutos
        else:
            return -minutos
    elif 'on time' in celda or 'scheduled' in celda:
        return 0
    else:
        return '-'

def calcular_diferencia(fila):
    try:
        dep = int(fila['dep_mins_of_delay'])
        arr = int(fila['arr_mins_of_delay'])
        return dep - arr
    except (ValueError, TypeError):
        return 0
