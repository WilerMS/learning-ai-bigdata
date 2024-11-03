# Ejercicios de Pandas

## Ejercicios Básicos

1. **Carga y Exploración del Dataset**
   - Carga el dataset en un DataFrame.
   - Muestra las primeras 2 filas del dataset.
   - Identifica el número de filas y columnas.
   - Observa los tipos de datos en cada columna.

2. **Resumen Estadístico**
   - Obtén un resumen estadístico de las columnas numéricas.
   - Genera un resumen estadístico solo para las columnas categóricas.

3. **Manejo de Datos Faltantes**
   - Cuenta el número de valores faltantes en cada columna.
   - Rellena los valores faltantes en la columna `cantidad` con la mediana.
   - Elimina las filas con valores nulos en `producto`.

4. **Renombrar Columnas**
   - Cambia el nombre de `Unnamed: 0` a `id`.
   - Haz que todos los nombres de columnas estén en minúsculas.
   - Renombra `categoria` a `tipo_producto`.

5. **Filtrar Datos**
   - Filtra las filas donde el `precio` sea mayor a 500.
   - Selecciona las filas donde `vendedor` sea "Juan".
   - Filtra las filas donde `ciudad` sea `Madrid` y el `rating` mayor a 0.5.

6. **Ordenar Datos**
   - Ordena el DataFrame por `precio` de mayor a menor.
   - Ordena por `fecha` en orden ascendente.
   - Ordena por `categoria` y luego por `precio` en orden descendente.

7. **Selección de Columnas y Filas**
   - Selecciona solo las columnas `producto` y `precio`.
   - Selecciona las filas de índice 10 a 20.
   - Obtén la columna `cantidad` como una Serie.

8. **Uso de loc e iloc**
   - Utiliza `.loc` para seleccionar las filas con `ciudad` igual a `Barcelona`.
   - Usa `.iloc` para seleccionar las primeras 5 filas y las primeras 3 columnas.

## Ejercicios Intermedios

9. **Agrupación de Datos**
   - Agrupa el DataFrame por `categoria` y calcula el promedio de `precio`.
   - Agrupa por `vendedor` y cuenta el número de ventas.
   - Agrupa por `ciudad` y calcula la suma de `cantidad`.

10. **Aplicar Funciones Personalizadas**
    - Crea una función que convierta el `precio` a euros (asume una tasa de cambio).
    - Aplica esta función a la columna `precio`.
    - Crea una columna nueva llamada `precio_euro` con los precios convertidos.

11. **Filtrado Avanzado**
    - Selecciona las filas donde el `rating` es menor que 0.3 y el `precio` es mayor que 600.
    - Filtra las filas donde el `comentarios` no esté vacío.
    - Filtra las filas donde `producto` contiene la palabra "laptop".

12. **Crear y Eliminar Columnas**
    - Crea una columna `ingreso` que sea el producto de `precio` y `cantidad`.
    - Elimina la columna `rating` del DataFrame.
    - Agrega una columna `descuento` con valores predeterminados de 0.1.

13. **Manejo de Fechas**
    - Convierte la columna `fecha` a formato de fecha.
    - Extrae el año de la columna `fecha` y crea una nueva columna `año`.
    - Filtra las ventas realizadas en 2023.

14. **Valores Únicos**
    - Encuentra todos los valores únicos en la columna `ciudad`.
    - Cuenta la cantidad de valores únicos en `categoria`.
    - Verifica cuántos vendedores únicos hay en el dataset.

15. **Aplicar Funciones Lambda**
    - Usa una función lambda para categorizar `rating` como `bajo`, `medio` o `alto`.
    - Crea una columna `comentario_largo` que indique si `comentarios` tiene más de 10 caracteres.

16. **Valores Faltantes Avanzados**
    - Rellena los valores faltantes en `comentarios` con el texto "Sin comentarios".
    - Rellena los valores de `precio` con el promedio de esa columna.

17. **Pivot Tables**
    - Crea una tabla pivote que muestre la suma de `cantidad` por `ciudad` y `categoria`.
    - Genera una tabla pivote que calcule el promedio de `precio` por `vendedor` y `año`.

## Ejercicios Avanzados

18. **Operaciones de Ventanas**
    - Crea una columna `media_movil` que calcule la media móvil de 3 días en `precio`.
    - Calcula el promedio de `cantidad` usando una ventana de tamaño 5.

19. **Merge y Join**
    - Crea un DataFrame de prueba con `vendedor` y `comisión`.
    - Realiza un merge del DataFrame principal con el nuevo DataFrame usando `vendedor`.

20. **Estadísticas Avanzadas**
    - Calcula la correlación entre `precio` y `rating`.
    - Encuentra el valor máximo y mínimo de `cantidad` por cada `ciudad`.

21. **Graficar con Pandas**
    - Realiza un gráfico de barras de `cantidad` por `categoria`.
    - Crea un histograma del `precio`.
    - Haz un gráfico de dispersión entre `precio` y `rating`.

22. **DataFrame de Muestra**
    - Extrae una muestra aleatoria del 10% de las filas.
    - Crea una muestra con 20 filas sin reemplazo.

23. **Trabajar con Series**
    - Convierte la columna `vendedor` en un objeto Series y aplica `.value_counts()`.
    - Usa `.map()` para reemplazar valores de `ciudad` (ej. "Barcelona" por "BCN").

24. **Condicionales y Transformaciones Complejas**
    - Crea una columna `nivel_precio` que sea "alto" si `precio` > 500 y "bajo" en caso contrario.
    - Establece `categoria` a "Otros" cuando esté vacío.

25. **Exportación de Datos**
    - Guarda el DataFrame en un archivo CSV con el nombre `ventas_limpio.csv`.
    - Exporta solo las columnas `vendedor`, `producto`, y `ingreso` a un nuevo archivo CSV.

