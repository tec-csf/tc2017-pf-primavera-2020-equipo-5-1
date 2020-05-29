# *PF5. Topología en estrella*
---
#### Materia: *Análisis y Diseño de Algoritmos*

##### Integrantes:
1. *Carla Pérez Gavilán Del Castillo* - *A01023033* - *CSF*
2. *Rubén Hernández Rivas* - *A01024669* - *CSF*
3. *Christian Alberto Dalma Schultz* - *A01423166* - *CSF*

---
## 1. Aspectos generales

Las orientaciones de la tarea se encuentran disponibles en la plataforma **Canvas**.

Este documento es una guía sobre qué información debe entregar como parte del proyecto, qué requerimientos técnicos debe cumplir y la estructura que debe seguir para organizar su entrega.

### 1.1 Requerimientos técnicos

A continuación se mencionan los requerimientos técnicos mínimos del proyecto, favor de tenerlos presente para que cumpla con todos.

* El equipo tiene la libertad de elegir las tecnologías de desarrollo a utilizar en el proyecto, sin embargo, debe tener presente que la solución final se deberá ejecutar en una de las siguientes plataformas en la nube: [Google Cloud Platform](https://cloud.google.com/?hl=es), [Amazon Web Services](https://aws.amazon.com/) o [Microsoft Azure](https://azure.microsoft.com/es-mx/).
* El proyecto deberá utilizar una interfaz Web.
* La arquitectura deberá estar separada claramente por capas (*frontend*, *backend*, *API RESTful*, datos y almacenamiento) según se necesite.
* Todo el código, *datasets* y la documentación del proyecto debe alojarse en este repositorio de GitHub. Favor de mantener la estructura de carpetas propuesta.

### 1.2 Estructura del repositorio

El proyecto debe seguir la siguiente estructura de carpetas, la cual generamos por usted:
```
- / 			        # Raíz de todo el proyecto
    - README.md			# Archivo con los datos del proyecto (este archivo)
    - frontend			# Carpeta con la solución del frontend (Web app)
    - backend			  # Carpeta con la solución del backend (CMS)
    - api			      # Carpeta con la solución de la API
    - datasets		  # Carpeta con los datasets y recursos utilizados (csv, json, audio, videos, entre otros)
    - dbs			      # Carpeta con los modelos, catálogos y scripts necesarios para generar las bases de datos
    - docs			    # Carpeta con la documentación del proyecto
```

### 1.3 Documentación  del proyecto

Como parte de la entrega final del proyecto, se debe incluir la siguiente información:

* Descripción del problema a resolver.
* Diagrama con la arquitectura de la solución.
* Descripción de cada uno de los componentes de la solución.
* Guía de configuración, instalación y despliegue de la solución en la plataforma en la nube seleccionada.
* Documentación de la API. Puede ver un ejemplo en [Swagger](https://swagger.io/). 
* El código debe estar documentado siguiendo los estándares definidos para el lenguaje de programación seleccionado.

## 2. Descripción del proyecto

**PROBLEMA 5: Topología Estrella**

El problema consiste en una computadora central que asigna trabajos de forma aleatoria a las computadoras perifericas siguiendo la siguiente estructura: 

![Topologia](/images/general.png)

El usuario debe poder insertar las siguientes variables para correr la simulación: 

* n --> cantidad de computadoras perifericas que se encuentran en la topología
* _&alpha; --> media por hora con distribución Poisson para distribución de trabajos en orden secuencial
* _&beta; --> 1/_&beta; será el tiempo promedio de falla de computadoras periféricas con distribución exponencial
* _&gamma; --> 1/_&gamma; indica el tiempo de falla de la computadora central con distribución exponencial. 
* _&delta; --> determina el tiempo de distriución de los trabajos 
* reboot --> tiempo que tarda en reiniciarse una computadora

A partir de estos parámetros se inicializa la computadora central cuyo trabajo consiste en asignar los trabajos de forma progresiva a las computadoras periféricas. Mientras estas computadoras no estén ocupadas o se encuentren en el proceso de recuperación después de una falla se ejecuta el trabajo. 

Cuando la computadora principal no está activa, o se encuentra en recuperación después de una falla, esta deja de distribuir trabajos, y los forma en una cola FIFO. 

## 3. Solución

A continuación aparecen descritos los diferentes elementos que forman parte de la solución del proyecto.

### 3.1 Arquitectura de la solución


![Topologia](/images/DiagramaAlgoritmos.jpeg)

Aquí se aprecia una opción simple y clara sobre todos los componentes de nuestra solución, las capas, las tecnologías y sobre todo el flujo continuo entre sus componentes. 

### 3.2 Descripción de los componentes

*[Incluya aquí una descripción detallada de cada uno de los componentes de la arquitectura así como una justificación de la selección de cada componente]*

### 3.3 Frontend

*[Incluya aquí una explicación de la solución utilizada para el frontend del proyecto. No olvide incluir las ligas o referencias donde se puede encontrar información de los lenguajes de programación, frameworks y librerías utilizadas.]*

#### 3.3.1 Lenguaje de programación

#### 3.3.2 Framework
#### 3.3.3 Librerías de funciones o dependencias




### 3.4 Backend

Existen dos clases principales las computadoras periféricas y la computadora central, cada una con su respectiva clase y constructor. 

#### THREADS

Estás clases se paralelizan de acuerdo al siguiente diagrama. Todas las computadoras periféricas tienen dos hilos de ejecución simultáneos.
 
 1. El primero de verifica constantemente si es que existe un trabajo a ejecutar, revisando la variable "current_job"
 2. El segundo de estos se encarga de enviar una falla en tiempos aleatorios a la computadora, y activar la bandera de failed. 

Mientras que las computadoras centrales cuentan con cuatro hilos en ejecución simultáneos: 
 
 1. Al igual que la computadora periferico este hilo se encarga de generar una falla en un tiempo aleatorio. 
 2. Este proceso genera la cantidad de hilos o procesos correspondiente a la cantidad de computadoras que el usuario indica que a su vez ejecutan los otros dos hilos que se mencionan anteriormente
 3. Este hilo se encarga de distribuir un hilo en un tiempo aleatorio, es decir sacarlo de la cola FIFO en la que se almacenan cuando no se pueden asignar a ninguna computadora periférica
 4. Este hilo se encarga de generar un trabajo cada cierto tiempo aletorio. 

![Hilos](/images/threads.png)

#### CLASES 
**PERIPHERAL** esta clase está compuesta por los 3 métodos que deben ejecutarse por cada una de las computadoras periféricas. 
**CENTRAL** esta clase trata de emular la computadora principal, que es capaz de generar trabajos en un tiempo aleatorio, fallar y distribuir estos mismos trabajos. A ella se conectan o inicializan las computadoras periféricas. 

![Classes](/images/classes.png)

#### TRABAJOS 
Existen tres método diferentes a ejecutar por las computadoras periféricas, a continuación se explica un poco acerca de su implementación de forma paralela: 
* Multiplicación de matrices: Se divide por filas para poder ejecutarse de forma paralela, cada fila por columna ocupa un hilo. Se utiliza ThreadPoolExecutor. 
_NOTA: la matriz por default tiene una dimensión de 4x4_   
* Suma de vectores: Cada suma de elemento a elemento es un hilo diferente en ejecución. 
_NOTA: los vectores tienen una dimensión de 10 elementos, que también puede ser editable._
* Producto punto de vectores: Cada multiplicación entre vectores y suma acumulada se ejecuta en un hilo diferente. 
    
![Jobs](/images/jobs.png)

#### 3.4.1 Lenguaje de programación 

Se utilizó Python 3.8.3. Se puede verificar la instalación en mac en el siguiente link: https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/

Aquí un ejemplo de main, se inicializa la computadora central indicando cuántas computadoras periféricas queremos incluir así como los valores indicados como parámetros los otros parámetros relevantes: el tiempo entre fallas, el tiempo para la distribución de  trabajos y el tiempo de generación de trabajos. 

```python
import star_topology
import time

def main():
    c = star_topology.Central(3, 4, 4, 4, 100)
    c.turn_on()
    time.sleep(50)
    c.turn_off()


if __name__ == '__main__':
    main()
```

#### 3.4.3 Librerías de funciones o dependencias

Se utilizaron dos librerías principales para el uso de paralelismo: 
- **concurrent.futures** : se utilizó el ThreadPoolExecutor para manejar una cantidad límitada de hilos que ejecuten una misma función de forma asíncrona. 
    - se utilizó en la función de multiplicación de matrices, suma de vectores y producto punto de dos vectores. 
    -  _FUENTE_: https://docs.python.org/3/library/concurrent.futures.html
- **threading** : se utilizó este modulo para manejar de manera manual las funciones concurrentes de la generación de trabajos, distribución de trabajos y manejo de fallas. 
    - _FUENTE_: https://docs.python.org/3/library/threading.html
- **time**: se utliza el método de sleep() para la espera de un proceso o entre fallas. 
    - _FUENTE_ :https://docs.python.org/3/library/time.html
 - **numpy**: se utiliza para generar números aleatorios con una distribución exponencial o poisson de acuerdo a los requerimientos del proyectos. 
    - para instalar:
   ```
    pip install numpy 
    # see more at https://pypi.org/project/numpy/
    ```
    - _FUENTE_: https://docs.scipy.org/doc/numpy-1.15.0/reference/routines.random.html

_FUENTE ÚTIL PARA MULTIPLICACIÓN DE MATRICES_: 
 - https://martin-thoma.com/part-iii-matrix-multiplication-on-multiple-cores-in-python-java-and-c/

### 3.5 API

*[Incluya aquí una explicación de la solución utilizada para implementar la API del proyecto. No olvide incluir las ligas o referencias donde se puede encontrar información de los lenguajes de programación, frameworks y librerías utilizadas.]*

#### 3.5.1 Lenguaje de programación
#### 3.5.2 Framework
#### 3.5.3 Librerías de funciones o dependencias

*[Incluya aquí una explicación de cada uno de los endpoints que forman parte de la API. Cada endpoint debe estar correctamente documentado.]*

*[Por cada endpoint debe incluir lo siguiente:]*

* **Descripción**:
* **URL**:
* **Verbos HTTP**:
* **Headers**:
* **Formato JSON del cuerpo de la solicitud**: 
* **Formato JSON de la respuesta**:


## 3.6 Pasos a seguir para utilizar el proyecto

*[Incluya aquí una guía paso a paso para poder utilizar el proyecto, desde la clonación de este repositorio hasta el despliegue de la solución en una plataforma en la nube.]*

## 4. Referencias

*[Incluya aquí las referencias a sitios de interés, datasets y cualquier otra información que haya utilizado para realizar el proyecto y que le puedan ser de utilidad a otras personas que quieran usarlo como referencia]*
