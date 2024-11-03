import pandas as pd
import numpy as np

NUM_OF_ROWS = 100

# Crear datos con errores intencionales
np.random.seed(42)

# Generar fechas
fechas = np.random.choice(
  pd.date_range(
    start='2023-01-01 00:00:00',
    end='2023-12-31 23:59:59',
    freq='H'
  ),
  size=100
)

# Generar datos base
data = {
  'fecha': fechas,
  'producto': np.random.choice(['Laptop', 'Monitor', 'Teclado', 'Mouse', 'Auriculares', None, 'laptop', 'MONITOR'], NUM_OF_ROWS),
  'categoria': np.random.choice(['Electrónica', 'electronica', 'ELECTRONICA', None, 'Electronca'], NUM_OF_ROWS),
  'precio': np.random.uniform(100, 1000, NUM_OF_ROWS),
  'cantidad': np.random.randint(-5, 50, NUM_OF_ROWS),  # Algunos valores negativos
  'vendedor': np.random.choice(['Ana', 'Juan', 'Wiler', 'Janise', 'Junel', 'María', 'maria', 'JUAN', '   Ana  ', None], NUM_OF_ROWS),
  'ciudad': np.random.choice(['Madrid', 'Barcelona', 'Valencia', ' madrid ', 'BARCELONA', None], NUM_OF_ROWS),
  'rating': np.random.uniform(0, 6, NUM_OF_ROWS),  # Algunos ratings fuera de rango (debería ser 0-5)
  'comentarios': np.random.choice(['Excelente', 'Bueno', 'Regular', 'Malo', '', ' ', None], NUM_OF_ROWS)
}

# Crear DataFrame
df = pd.DataFrame(data)

# Convertir a CSV con algunos errores de formato
print(df)
df.to_csv('ventas.csv')