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

Se genera un python con un backend que forma a través de librerías que permiten el paralelismo como lo son threading y ThreadPoolExecutor, lo cual se explica con mayor detenimiento en la parte de *Backend*. Se utiliza flask para poder pasar los valores de input del usuario para poder a través del constructor, generar la computadora Central. Esta computadora Central estará agregando a una cola constantemente, a través de flask se vacía esta cola creando updates cada 1000 milisegundos. 

En el python llamado star_test.py se brinda otro backend que regresa en vez de strings ints con el fin de facilitar las animaciones en el html junto con javascript:

Peripheral | explanation | 
--- | --- | 
0 | starting failing | 
1 | rebooted after fail  | 
2 | job assignment on computer | 
3 | executing vector sum | 
4 | executing dot product | 
5 | executing multiply matrix | 
6 | job not found | 

Central | explanation | 
--- | --- | 
0 | starts failing  | 
1 | failing ends  | 
2 | generate job | 
3 | distribute job | 
4 | job not identified | 

### 3.1 Arquitectura de la solución


![Topologia](/images/DiagramaAlgoritmos.jpeg)

Aquí se aprecia una opción simple y clara sobre todos los componentes de nuestra solución, las capas, las tecnologías y sobre todo el flujo continuo entre sus componentes. 

### 3.2 Descripción de los componentes

*BACKEND*: se encarga a través de un código en python de ejecutar las funciones en las computadoras periféricas que están recibiendo trabajos por parte de la computadora central. El código hace uso de paralelismo, y está implementado con los modulos de python establecidos en la sección de "dependencias" del "backend". 

### 3.3 Frontend

Para crear el Frontend utilizamos el lenguaje HTML y ademas utilizamos 2 librerias externas para expresar de mejor manera nuestro algoritmos 

#### BOOTSRAP

Bootsrap la utilizamos como nuestro framework principal, es una libreria externa la cual nos da mayor libertad de expresarnos de forma mas creativa por nuestro frontend, debido a que cuenta con un archivo de estilos y funciones ya creada, listas para ser utilizadas en el framework, de esta forma logramos crear una pagina muy bien hecha donde el usuario puede ver claramente como se utiliza

![front](/images/frontend1.png)

#### P5.JS

P5.js es un programa de java script basado en procesing para crear visualicaciones en HTML, es un programa muy sencillo de usar donde tenemos nuestro sketch.js y lo llamamos dentro de nuestro HTML con las especificaicones que querramos. es un programa muy sencillo con funciones bien documentadas y que recomiendo mucho

![front2](/images/frontend2.png)

#### 3.3.1 Lenguaje de programación

Para el desarollo de lo que integra la back-end se utilizó solamente Python debido a su sencillez para tratar temas complejos de funciones y sobre todo una caracteristica única de este proyecto la cual es paralelismo. A consecuencia de esto la conexión entre backend y frontend fue igualmente programada con Python implementando un framework llamado Flask. 

EL lenguaje de programacion utilizado principalmente para el front end fue *HTML* y *Java Script*.

#### 3.3.2 Framework
Para realizar una conexión entre el back-end y el front-end se utilizó Flask, el cual es un "micro" Framework para desarrollar cualquier aplicación básica de una forma ágil y rápida. Este inlcuye un servidor web de desarrollo, por lo tanto no necesita de una infraestructura con un servidor para poder estar probando el funcionamiento de las aplicaciones, inclusive asi fue como se realizó esto para el proyecto, desde el servidor web y desplegando la interfaz web directamente en sevidor local "localhost" para realizar pruebas. 
Lo mas importante por lo que se utilizó este framework es por su compatibilidad con Python ya que ese fue el lenguaje con el que se desarrollo nuestro back-end, aunque en algunos html's de prueba se implementaron funciones en javascript, siempre se busco una homologación en todo el proyecto.
El Framework principal utilizado fue Bootstrap lo cual fue muy sencillo ya qu ees uno de los frameworks mas utilizados y mas sencillos para el publico.

Es necesario instalar Flask para poder implementarlo en los programas, a continuación dejo los comandos y documentación pertinente:

Para Python3: 
```
pip3 install flask 
```
Para Python2:
```
pip install flask
```

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
Como lenguaje de programación utilizado para el back-end y su conexión con el front-end se utilizo **Python** en su versión 3.8.3 y posterior. Python es un lenguaje de programación creado en 1991. Este hasta la actualidad es desarrollado como un proyecto de código abierto, administrado por Python Software Foundation. Cuenta con un versiones superiores a 3.8.0 y versiones descontinuadas apenas este año 2020 como lo es el famoso Python 2.7. La extensión de los archivos creados con python es **.py.** 
#### 3.5.2 Framework
Tratando sobre el framework con el cual fue construido la conexión entre el back-end con el front-end, ya se puede encontrar una explicación mas detallada en la parte superior del READ ME, todo acerca de FLASK y su documentación. 
#### 3.5.3 Librerías y módulos de funciones o dependencias
Bootstrap: Biblioteca multiplataforma de codigo abierto para diseño de sitios y aplicaciones web. Contiene gran variedad de plantillas de diseño con tipografía, formularios, botones, cuadros, menús de navegación y otros elementos de diseño, basado en HTML Y CSS. 
Webrowser: Módulo que incluye funciones para poder abrir URL's en navegadores de forma interactiva, esta incluye un registro de los navegadores disponibles en casa de contar con varias opciones en el sistema.
Flask: Framework y dependencias (explicados mas arriba)
Concurrent.futures: Este módulo permite una interfaz de alto nivel para ejecutar callables de manera asíncrona, esta ejecución puede ser performada a base de threads (programación paralela).
#### 3.5.4 Metodos
Para poder extraer inputs de data dentro de nuestra interfaz web y poderlos insertar como parametros dependientes de nuestro codigo base fue necesario hacer uso de dos metodos muy populares dentro del protocolo HTTP:

**GET:** Se refiere a obtener información de un servidor, trae datos que se encuentran en este servidor ya sea un archivo o una base de datos al cliente. Es necesario enviar un identificador que nos permita obtener esta información de vuelta, conocido como "request". 

**POST:** Este se refiere al envio de información desde el cliente para que esta pueda ser procesada y actualizada en el servidor. Cuando se envía un request de datos a traves de un formulario, son procesados y a traves de una redireccion por ejemplo "response" se devuelve una página de información, esto es el uso del metodo POST.  

*[Incluya aquí una explicación de cada uno de los endpoints que forman parte de la API. Cada endpoint debe estar correctamente documentado.]*

*[Por cada endpoint debe incluir lo siguiente:]*

* **Descripción**:
* **URL**:
* **Verbos HTTP**:
* **Headers**:



## 3.6 Pasos a seguir para utilizar el proyecto

En caso de que quisiera correr el backend por separado: 
1. Descargar las dependencias: python, numpy 
2. Correr el código con python3
3. Recuerda tener el main como se muestra en la sección de "backend"

Para probar la implementación de conexión entre back-end y front-end se diseño un archivo en python:

```
dynamic1.py
```
Y se diseñaron dos archivos prueba en html ubicados en la carpeta templates (es indispensable que se encuentren ahi todos los archivos html, para que flask funcione correctamente debido a su implementación de jinja2 
```
index.html dy1.html
```
Para poder correr los programas es necesario llevar algunos pasos para correr el programa y poder realizar una conexión entre el backend y la interfaz web, unos de ellos ya configurados en la Maquina Virtual sin embargo importantes a ser mencionados). 

**Importación de Librerias directamente en código:**
```
from flask import Flask, jsonify, render_template, request, session, redirect, url_for
from flask_bootstrap import Bootstrap
import webbrowser
import time
import star_test
from flask_wtf import FlaskForm
import threading
import concurrent.futures
```
**Entorno Virtual:**

1. Instalar un entorno virtual
```
$ pip install virtualenv
```
2. Crear un entorno virtual
```
$ py -3 -m venv venv
```
3. Activar un entorno virtual 
```
venv\Scripts\activate 
```
4. Para compilar el programa
```
set FLASK_APP=dynamic1.py
```
5. Correr el programa
```
flask run
```
Aun asi se anexa una guía oficial proveniente de la documentación de Flask:
https://flask.palletsprojects.com/en/1.1.x/installation/

## 4. Referencias

*[Incluya aquí las referencias a sitios de interés, datasets y cualquier otra información que haya utilizado para realizar el proyecto y que le puedan ser de utilidad a otras personas que quieran usarlo como referencia]*

Pregunta actualmente de una cuenta de integrante del equipo en StackOverflow:
https://stackoverflow.com/questions/62110427/how-to-pass-data-variable-from-a-python-flask-code-to-another-python-code/62111328#62111328

https://flask.palletsprojects.com/en/1.1.x/
https://flask.palletsprojects.com/en/1.1.x/installation/
https://www.ecured.cu/Python
http://blog.micayael.com/2011/02/09/metodos-get-vs-post-del-http/



