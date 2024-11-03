# Pandas

Pandas es una librería de python para el manejo y análisis de grandes estructuras de datos de forma eficiente, permitiendo limpiar, filtrar, transformar y analizar datos de manera sencilla.

## Estructuras de datos

Pandas se basa en dos estructuras de datos principales:
- **Series**: Unidimensionales, son similaries a una lista de python o a una columna de una hoja de calculo. 
- **Dataframes**: Bidimensionales, son similares a una matriz o una tabla completa de excel, ya que se compone de filas y columnas.

## Tipos de datos

Pandas maneja varios tipos de datos:
- **int64**: Enteros
- **float64**: Números con decimales
- **object**: Cadenas de texto
- **datetime**: Fechas y horas
- **bool**: Valores True o False

## Operaciones comunes en Pandas

- **Cargar dato de diversas fuentes**: Pandas permite cargar datos de archivos CSV, Excel, JSON, Bases de datos y más.
```python
  # Cargar datos de un archivo CSV
  df_csv = pd.read_csv('archivo.csv')  
  # Cargar datos desde un archivo JSON
  df_json = pd.read_json('archivo.json') 
  # Cargar datos desde un archivo de Excel
  df_excel = pd.read_excel('archivo.xlsx', sheet_name='Hoja1') 
  # Cargar datos desde una tabla SQL
  df_sql = pd.read_sql_query('SELECT * FROM mi_tabla', conexion) 
```

- **Guardar datos en diversos formatos**: Pandas permite guardar datos en diferentes formatos o archivos. Entre ellos, CSV, JSON, HTML, EXCEL...
```python
  # Guardar DataFrame en un archivo CSV
  df.to_csv('archivo_salida.csv', index=False)
  # Guardar DataFrame en un archivo JSON
  df.to_json('archivo_salida.json', orient='records')  
  # Guardar DataFrame en un archivo Excel
  df.to_excel('archivo_salida.xlsx', sheet_name='Hoja1', index=False)
  # Guardar DataFrame en un archivo HTML
  df.to_html('archivo_salida.html', index=False)
```

- **Exploración de datos**: Pandas permite ver rápidamente la estructura de los datos.
```python
  dataframe.head() # muestra las primeras filas
  dataframe.info() #resumen de las columnas y sus tipos de datos
  dataframe.describe() # estadísticas descriptivas de las columnas numéricas
```