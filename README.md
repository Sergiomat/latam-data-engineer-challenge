# LATAM Data Engineer Challenge

Este repositorio contiene las soluciones al desafío de data engineering de LATAM. El desafío consiste en resolver tres problemas diferentes usando dos enfoques por cada problema: uno optimizando el tiempo de ejecución y otro optimizando el uso de memoria. A continuación, se detallan las soluciones implementadas, así como sugerencias de mejoras y una guía paso a paso para realizar las pruebas en un entorno AWS.

[Descargar el archivo grande](https://latam-challenge.s3.amazonaws.com/farmers-protest-tweets-2021-2-4.json)

## Problema 1: Top 10 fechas con más tweets

### Enfoques Implementados
1. **Optimización de tiempo de ejecución (`q1_time`)**
2. **Optimización de uso de memoria (`q1_memory`)**

### Funciones Implementadas
```python
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Implementación para optimizar el tiempo de ejecución
    pass

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Implementación para optimizar el uso de memoria
    pass
```

### Sugerencias de Mejora

####    * Optimización de tiempo de ejecución:
        1) Implementar el procesamiento paralelo utilizando librerías como multiprocessing o dask.
        2) Utilizar índices en las columnas de fecha para acelerar las consultas.
####    * Optimización de uso de memoria:
        1) Leer los datos en chunks pequeños y procesarlos de manera incremental.
        2) Usar tipos de datos más eficientes para las columnas del DataFrame.

## Problema 2: Top 10 emojis más usados

### Enfoques Implementados
1. **Optimización de tiempo de ejecución (`q2_time`)**
2. **Optimización de uso de memoria (`q2_memory`)**

### Funciones Implementadas
```python
def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Implementación para optimizar el tiempo de ejecución
    pass

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # Implementación para optimizar el uso de memoria
    pass
```

### Sugerencias de Mejora

####    * Optimización de tiempo de ejecución:
        1) Utilizar expresiones regulares compiladas para una búsqueda más rápida de emojis.
        2) Emplear procesamiento paralelo para analizar el contenido de los tweets.
####    * Optimización de uso de memoria:
        1) Procesar los tweets en pequeñas porciones para evitar cargar todo el conjunto de datos en memoria.
        2) Usar estructuras de datos más ligeras, como generadores, en lugar de listas.

## Problema 3: usuarios más influyentes

### Enfoques Implementados
1. **Optimización de tiempo de ejecución (`q3_time`)**
2. **Optimización de uso de memoria (`q3_memory`)**

### Funciones Implementadas
```python
def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Implementación para optimizar el tiempo de ejecución
    pass

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Implementación para optimizar el uso de memoria
    pass
```

### Sugerencias de Mejora

####    * Optimización de tiempo de ejecución:
        1) Utilizar estructuras de datos eficientes como Counter de la biblioteca collections.
        2) Emplear consultas paralelas para contar las menciones.
####    * Optimización de uso de memoria:
        1) Procesar los datos en pequeños segmentos para reducir el uso de memoria.
        2) Almacenar temporalmente los conteos en una base de datos ligera como SQLite.

## Ejecución en un Entorno AWS

### Paso a Paso:

1) Configuración del Entorno

    * Crear una instancia EC2 en AWS.
    * Instalar Python y las dependencias necesarias
    
    ```sh
    sudo apt update
    sudo apt install python3-pip
    pip3 install pandas memory-profiler matplotlib seaborn dask emoji
    ```

2) Subida de Archivos

    * Subir los archivos de datos a un bucket S3.
    * Configurar las credenciales AWS en la instancia EC2

    ```sh
    aws configure

3) Descarga de Datos desde S3

    * Descargar el archivo de datos desde el bucket S3
    
    ```sh
    aws s3 cp s3://<bucket-name>/data/farmers-protest-tweets-2021-2-4.json .

4) Ejecución de las Funciones

    * Ejecutar el Jupyter Notebook en la instancia EC2

    ```sh
    jupyter notebook --ip=0.0.0.0 --no-browser
    ```

    * Acceder al notebook desde el navegador y realizar las pruebas ejecutando las celdas correspondientes.

5) Medición de Tiempos y Memoria

    * Para medir el tiempo de ejecución, utilizar time:

    ```python
    import time
    start_time = time.time()
    # Llamada a la función
    end_time = time.time()
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")
    ```

    * Para medir el uso de memoria, utilizar memory-profiler

    ```python
    from memory_profiler import memory_usage
    mem_usage = memory_usage((func, (file_path,)))
    print(f"Uso de memoria: {max(mem_usage) - min(mem_usage)} MiB")
    ```
    