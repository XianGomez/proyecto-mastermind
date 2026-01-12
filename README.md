<div align="center">

# Tabla de contenido

</div>

<div style="font-size: 20px;">

- [**Introducción**](#introducción)
- [**Metodología**](#metodología)
- [**Manual**](#manual)
    - [**Instalación**](#instalación)
- [**Descripción técnica**](#descripción-técnica)
    - [**Historias de usuario**](#historias-de-usuario)
    - [**Arquitectura de la aplicación**](#arquitectura-de-la-aplicación)
-  [**Diseño**](#diseño)
    - [**Diagrama de Componentes**](#diagrama-de-componentes)
- [**Implementación**](#implementación)
    - [**Tecnologías y Herramientas utilizadas**](#tecnologías-y-herramientas-utilizadas)
    - [**Backend**](#backend)
    - [**Frontend**](#frontend)
- [**Pruebas**](#pruebas)
    - [**Test de unidad**](#test-de-unidad)
    - [**Test de integración**](#test-de-integridad)
- [**Análisis del tiempo invertido**](#análisis-del-tiempo-invertido)
    - [**Wakatime**](#wakatime)
    - [**Justificación temporal**](#justificación-temporal)
- [**Uso de la IA**](#uso-de-la-ia)
- [**Conlusión**](#conclusión)
    - [**Posibles mejoras**](#posibles-mejoras)
    - [**Dificultades**](#dificultades)

</div>

# Introducción
Érika Sousa - [Érika](https://github.com/erikadocus-web)  
Xian Gomez - [Xian](https://github.com/XianGomez)

Somos alumnos de Desarrollo de Aplicaciones Multiplataforma en el IES de Teis.  
Este proyecto se ha realizado como una muestra de nuestro aprendizaje de dos meses y medio de python, markdown y git.

El juego Mastermind es un problema clásico de lógica que consiste en descubrir una combinación secreta a partir de una serie de intentos y pistas parciales. En este proyecto, se propone una versión del juego en la que el usuario establece el código secreto, mientras que la máquina actúa como jugador, intentando adivinar la combinación correcta mediante el uso de un algoritmo genético.
El algoritmo genético es una técnica de inteligencia artificial inspirada en los principios de la evolución natural, como la selección, la cruza y la mutación. A partir de una población inicial de posibles soluciones generadas aleatoriamente, el sistema evalúa cada individuo según su cercanía al código secreto y selecciona los más aptos para reproducirse y generar nuevas generaciones de combinaciones cada vez más precisas.
El objetivo del proyecto es implementar un sistema capaz de descubrir el código secreto definido por el usuario en el menor número posible de generaciones, demostrando así la eficiencia de los algoritmos genéticos para resolver problemas de búsqueda en espacios grandes y complejos.

# Metodología
El tipo de metodología usado en este proyecto ha sido una mezcla de desarrollo en ***Espiral***.
Hemos empezado desarrollando el proyecto con el modelo en ***Espiral***. Este método lo hemos usado para realizar todas las historias de usuario hasta llegar a un prototipo.

Por último, hemos usado ***Scrum*** como marco de trabajo durante todo el proyecto.

# Manual

## Instalación

### Entorno Virtual - Windows

1. Abrimos una terminal y en ella escribiremos lo siguiente:  
    - **``py -m venv venv``** con esto se ha creado un entorno virtual llamado **``venv``**.  

    <img src="images/venv.png" alt="Comando para crear entorno virtual llamado venv" width="500px" height="350px"><br>

2. Ahora toca activar el entorno virtual y para ello hacemos lo siguiente:
    - En la terminal escribimos lo siguiente **``cmd``**.
    - Luego se escribirá **``.\venv\Scripts\activate.bat``**.  

    <img src="images/activar_venv.png" alt="Comando para activar el entorno virtual"><br>

# Descripción técnica

## Historias de usuario
![Historia de usuario](images/historia1.png)  

![Historia de usuario](images/historia2.png)

## Arquitectura de la aplicación

La arquitectura que se ha utilizado para este proyecto es el de MVC más servicios.  
 - En el **modelo** nos encontramos con los parametros a seguir.
 - En la **vista** nos encontramos con lo que el usuario ve en su navegador.
 - En el **controlador** coordina las acciones entre la vista y el modelo.
 - En el **servicio** contiene funciones o clases que encapsulan lógica de negocio.


# Diseño

## Diagrama de Componentes

[![Diagrama de dependencias](images/diagrama.png)](images/venv.png)


# Implementación
## Tecnologías y Herramientas utilizadas

- [Python](https://docs.python.org/3.12/)
    - [Venv](https://docs.python.org/es/3/library/venv.html)
    - [Markdown](https://python-markdown.github.io/)
    - [Pytest](https://docs.pytest.org/en/stable/)
- [Git](https://git-scm.com/)

## Backend

- Python

Los módulos usados para backend en nuestro proyecto son:
- Modelo
- Servicios
- Controlador

## Frontend

El módulo usado para frontend en nuestro proyecto es:
- Vista

El módulo de vista, implementado en el archivo visualización, es el encargado de proporcionar la interfaz de interacción entre el usuario y el sistema. Su función principal es permitir que el usuario introduzca el código secreto y observar en tiempo real cómo el algoritmo genético ejecuta el proceso de búsqueda hasta encontrar la combinación correcta.
La interfaz solicita al usuario que ingrese la combinación secreta respetando las reglas del juego (longitud del código y rango de valores permitidos). Una vez ingresado el código, el módulo se encarga de validar los datos y enviarlos al módulo de lógica para iniciar la ejecución del algoritmo genético.
Este módulo se diseñó con una estructura simple e intuitiva, facilitando la comprensión del funcionamiento del algoritmo y permitiendo al usuario observar de forma didáctica cómo la inteligencia artificial resuelve el problema.

# Pruebas
## Test de unidad

Es una técnica de prueba de software que nos permite comprobar funciones o métodos de manera individual, en nuestro caso tenemos 7 test de unidad:
![Imagen de test de unidad](images/pytest.jpeg)

## Test de integridad

No se ha implementado ningún test de integración

# Análisis del tiempo invertido

## Wakatime

### Érika

![Tiempo total invertido](images/erika.png)

### Xian

![Tiempo total invertido](images/xian.jpeg)

## Justificación temporal

La duración del proyecto ha sido de unas tres semanas. En las cuales los primeros días se utilizo para la comprensión del proyecto en si, además de estudiar como organizar el proyecto, después de entenderlo empezamos a llevarlo a cabo y los últimos días los usamos para hacer la documentación.  

# Uso de la IA

1. ¿Qué herramienta de IA generativa usaste (nombre y versión)?
    - La herramienta de IA generativa usamos fue ChatGPT 4-o o Copilot
2. ¿Qué tipos de prompts proporcionaste?
    - Cuando nos encontrabamos con un bug que no eramos capaces de resolver, se le pedía ayuda para entender cual era el problema.
3. ¿Para qué usaste la herramienta?
    - Añadir los casos test
    - Añadir visualizacion.py
    - Bugs incapaces de dar solución después de horas de intento
4. ¿Cómo has utilizado o cambiado la salida de la IA generativa?
    - En los demás casos las soluciones que nos podia ofrecer ChatGPT no eran validas a nuestro proyecto, pero nos daba pistas por donde podemos tirar y nos daba ejemplos.

# Conclusión

En este proyecto hemos puesto en práctica los conocimientos adquiridos durante los primeros 2 meses y medio enseñados en las clases de programación y entornos de desarrollo.

## Posibles mejoras

Añadir una opción en la que juegue el usuario y que el código secreto lo seleccionara la máquina.

Se puede también hacer mejoras tanto visuales.

## Dificultades

Las dificultades que tuvimos fue principalmente encontrar el enfoque del proyecto y tener una visión de lo que teniamos que hacer.
