# Ejercicios de Análisis de Datos - Dataset de Ventas

## NIVEL BÁSICO - Exploración y Limpieza Simple
1. Muestra las dimensiones del DataFrame y sus primeras y últimas filas
2. Identifica cuántos valores nulos hay en cada columna
3. ¿Cuántos productos únicos hay en el dataset?
4. Elimina los espacios en blanco extra en las columnas de texto
5. Convierte todos los nombres de productos a minúsculas
6. Reemplaza los valores nulos en la columna 'comentarios' por "Sin comentarios"
7. Muestra un resumen estadístico básico del DataFrame
8. Lista todos los vendedores únicos con sus variantes
9. Calcula el número total de ventas
10. Identifica las ciudades con datos faltantes

## NIVEL INTERMEDIO - Limpieza y Transformación
11. Estandariza los nombres de vendedores (Ana, ANA, ana → Ana)
12. Corrige los valores negativos en la columna 'cantidad' sustituyéndolos por 0
13. Asegúrate que la columna 'rating' solo contenga valores numéricos entre 0 y 5
14. Corrige los errores en la columna 'precio' y conviértela a tipo float
15. Arregla las fechas inválidas en la columna 'fecha'
16. Crea una nueva columna 'monto_total' multiplicando precio por cantidad
17. Estandariza los nombres de las categorías y corrige "Electronca"
18. Crea una columna 'mes' y otra 'día_semana' a partir de la fecha
19. Identifica y corrige valores atípicos en la columna 'precio'
20. Crea una columna 'descuento' que sea True si el precio está por debajo del promedio de su categoría

## NIVEL AVANZADO - Análisis y Agrupación
21. Calcula el total de ventas por vendedor y ordena de mayor a menor
22. Encuentra el producto más vendido por ciudad
23. Calcula el precio promedio por categoría
24. Identifica los días con mayores y menores ventas
25. Calcula el rating promedio por producto
26. Genera una tabla pivote que muestre las ventas por mes y categoría
27. Analiza la distribución de ventas por día de la semana
28. Calcula el porcentaje de participación de cada producto en las ventas totales
29. Encuentra la combinación producto-ciudad con mejor rating promedio
30. Identifica los períodos de 3 días consecutivos con mayores ventas

## NIVEL EXPERTO - Análisis Complejo
31. Crea una columna nueva que categorice las ventas en "Alta", "Media" y "Baja" según percentiles
32. Identifica patrones de venta semanales: ¿qué días se vende más?
33. Calcula la evolución del precio promedio por categoría a lo largo del tiempo
34. Identifica vendedores con comportamiento atípico
35. Analiza la correlación entre rating y cantidad vendida
36. Crea un indicador de rendimiento por vendedor
37. Desarrolla un análisis de estacionalidad en las ventas
38. Calcula la tasa de crecimiento mensual por categoría
39. Identifica productos con tendencia de ventas decreciente
40. Analiza el impacto del rating en las ventas futuras

## NIVEL MAESTRO - Análisis Avanzado y Reporting
41. Identifica tendencias estacionales en las ventas por categoría
42. Crea un sistema de detección de anomalías para transacciones sospechosas
43. Genera un reporte completo de KPIs por vendedor
44. Desarrolla un análisis de cohortes por mes de primera venta
45. Crea un sistema de puntuación para productos
46. Implementa un análisis de cesta de compra básico
47. Calcula la probabilidad de venta por día y hora
48. Desarrolla un modelo simple de predicción de ventas
49. Crea un sistema de clasificación de comentarios
50. Analiza la rentabilidad por producto y categoría

## RETOS DE VISUALIZACIÓN
51. Crea un gráfico de calor de ventas por día y hora
52. Visualiza la distribución de precios por categoría con boxplots
53. Genera un gráfico de barras apiladas de ventas por categoría y ciudad
54. Crea un gráfico de líneas de la evolución temporal de ventas
55. Visualiza la correlación entre variables numéricas

## RETOS DE AUTOMATIZACIÓN
56. Crea una función que limpie automáticamente nuevos datos
57. Desarrolla un pipeline de procesamiento completo
58. Implementa validaciones automáticas de datos
59. Crea un generador automático de reportes
60. Desarrolla un sistema de alertas para valores atípicos

## RETOS DE INTEGRACIÓN
61. Combina el análisis con datos externos (por ejemplo, días festivos)
62. Crea un sistema de recomendación básico
63. Implementa un scoring de clientes
64. Desarrolla un análisis de segmentación de productos
65. Crea un dashboard interactivo con los KPIs principales

## RETOS DE OPTIMIZACIÓN
66. Optimiza el rendimiento del código de limpieza
67. Mejora la eficiencia del análisis de datos
68. Implementa procesamiento en paralelo donde sea posible
69. Optimiza el almacenamiento de datos
70. Crea funciones reutilizables para análisis comunes

_Nota: Se recomienda resolver los ejercicios en orden de dificultad y documentar el proceso y decisiones tomadas en cada paso._