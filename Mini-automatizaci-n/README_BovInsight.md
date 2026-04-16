# BovInsight - Automatización de Análisis Ganadero

Proyecto orientado al **análisis automatizado de datos ganaderos** a partir de un archivo CSV realista.  
El sistema lee los registros, valida columnas clave, limpia datos, calcula indicadores, identifica alertas y genera un reporte automático listo para revisión.

## Objetivo

Transformar un conjunto grande de registros ganaderos en información útil y verificable mediante un script en Python que:

- lea el archivo de datos;
- valide la estructura esperada;
- calcule estadísticas descriptivas;
- analice alertas, salud y producción;
- genere archivos de salida para apoyar la interpretación de resultados.

## Nombre sugerido para el repositorio

`bovinsight-analisis-ganadero`

## Archivos principales

- `analisis_ganadero.py` → script principal de automatización
- `datos_ganaderos_realistas_analisis_59172.csv` → dataset de entrada
- `README.md` → descripción del proyecto

## Estructura recomendada

```bash
bovinsight-analisis-ganadero/
├── analisis_ganadero.py
├── datos_ganaderos_realistas_analisis_59172.csv
├── README.md
└── salidas/
```

## Requisitos

- Python 3.10 o superior
- pandas

Instalación rápida:

```bash
pip install pandas
```

## Cómo ejecutar

### Opción 1: usando el nombre por defecto del CSV
```bash
python analisis_ganadero.py
```

### Opción 2: indicando la ruta del archivo CSV
```bash
python analisis_ganadero.py datos_ganaderos_realistas_analisis_59172.csv
```

## Qué hace el script

El script realiza automáticamente las siguientes tareas:

1. **Carga el archivo CSV** y verifica que exista.
2. **Valida columnas esenciales** del dataset.
3. **Convierte tipos de datos** numéricos y fechas.
4. **Calcula indicadores generales**, como:
   - total de registros
   - total de animales únicos
   - total de fincas
   - rango de fechas
5. **Analiza variables numéricas**, como:
   - peso
   - edad
   - condición corporal
   - producción de leche
   - consumo de materia seca
   - agua
   - costo de alimentación
6. **Resume variables categóricas**, como:
   - sistema de producción
   - raza
   - categoría animal
   - estado de salud
   - alerta principal
   - departamento
7. **Detecta alertas analíticas**, por ejemplo:
   - registros con peso bajo
   - animales en observación
   - alertas principales distintas de “Sin novedad”
   - registros con valores faltantes en columnas críticas
8. **Genera archivos de salida** en la carpeta `salidas/`.

## Archivos de salida esperados

Al ejecutar el proyecto, se generan:

- `salidas/reporte_analisis_ganadero.txt`
- `salidas/resumen_numerico.csv`
- `salidas/faltantes_por_columna.csv`
- `salidas/resumen_alertas.csv`
- `salidas/promedio_peso_por_categoria.csv`
- `salidas/promedio_leche_por_raza.csv`

## Resultado esperado

Al finalizar la ejecución:

- el script debe correr sin errores;
- debe crear la carpeta `salidas/` si no existe;
- debe generar los archivos de análisis;
- el reporte de texto debe resumir los hallazgos principales;
- los resultados deben coincidir con los datos procesados.

## Cómo verificar resultados

Para validar que la automatización funciona correctamente, se recomienda revisar:

1. Que el número de registros cargados coincida con el CSV.
2. Que el total de animales únicos no sea mayor que el total de registros.
3. Que los promedios calculados sean coherentes con los rangos del dataset.
4. Que las alertas contadas en `resumen_alertas.csv` coincidan con lo observado en el archivo original.
5. Que los archivos de salida hayan sido creados correctamente.

## Posibles mejoras futuras

- agregar gráficos automáticos;
- generar reportes en Excel o PDF;
- incorporar análisis por finca o municipio;
- crear un panel web para consultar resultados;
- comparar periodos de tiempo y evolución por animal.

## Propósito académico

Este proyecto permite trabajar temas como:

- ejecución de scripts;
- automatización de análisis de datos;
- validación de resultados esperados;
- manejo de archivos CSV;
- uso de estructuras condicionales y ciclos;
- generación de evidencias para repositorio.

## Analisis del trabajo realizado 

En este proyecto desarrollé un programa en Python que permite analizar datos ganaderos a partir 
de un archivo CSV. El sistema carga la información, valida que los datos sean correctos, realiza
conversiones necesarias y ejecuta un análisis automático para generar reportes.

Además, el programa organiza los resultados en diferentes archivos, facilitando su lectura e
interpretación.

### ¿Qué se observó?

Durante la ejecución del programa se pudo observar que:

- Los datos fueron cargados correctamente sin errores.
- Se procesaron más de 50,000 registros de información ganadera.
- El sistema identificó correctamente valores faltantes y datos inconsistentes.
- Se generaron estadísticas claras sobre peso, producción de leche y costos.
- Se detectaron alertas importantes como animales con bajo peso o en observación.

Esto demuestra que el programa funciona de manera eficiente y logra procesar grandes volúmenes
de información.

### ¿Qué resultados se esperaban?

Se esperaba que el sistema fuera capaz de:

- Leer correctamente el archivo CSV
- Validar la estructura de los datos
- Generar estadísticas confiables
- Detectar posibles problemas en los datos (alertas)
- Crear archivos de salida organizados automáticamente

Finalmente, los resultados obtenidos cumplieron con lo esperado, ya que el programa generó
correctamente los archivos de resumen y el reporte final en la carpeta "salidas", permitiendo
analizar la información de forma clara y ordenada.

# Autor 

Alejandra Valencia Villa