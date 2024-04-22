# Mantenimiento de Usuarios - Aplicación CRUD
Esta es una aplicación desarrollada en Python utilizando Flask para el mantenimiento de una tabla específica. La aplicación permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una tabla:

## Repositorio
### Descripción
Este repositorio contiene el código fuente de la aplicación de mantenimiento de tabla desarrollada como parte del desafío "backend-python nivel 1".

## Alcances del Desarrollo
Se ha alcanzado el nivel 4 del desafío, cumpliendo con todos los requisitos especificados.
### Nivel 1 (Creación):
Se han creado APIs para realizar operaciones CRUD sobre la tabla:
* GET: Para listar todos los registros.
* GET: Para obtener un registro específico.
* POST: Para añadir un nuevo registro.
* PUT: Para actualizar un registro específico.
* DELETE: Para eliminar un registro específico.
### Nivel 2 (Reglas):
Se han implementado reglas donde los campos name, lastname, y email son obligatorios para la creación y actualización de registros.

### Nivel 3 (Documentación):
Se ha documentado las APIs utilizando Swagger para facilitar su comprensión y uso. La documentación se puede encontrar en enlace a la documentación Swagger.

### Nivel 4 (Portabilidad):
Se ha creado un archivo Dockerfile que permite generar una imagen de la aplicación para su fácil despliegue en diferentes entornos.

## Ejecución de la Solución
Para ejecutar la solución, sigue estos pasos:
* Clona este repositorio en tu máquina local.

### Ejecutarlo con DOCKER:
> Antes que nada asegurate de tener instalado DOCKER en tu maquina.
Ejecuta los siguientes comandos:
* Para construir el contenedor usa `docker build -t flaskapp .``
* Para correr el contenedor usa `docker run -it -p 5000:5000 flaskapp`

### Ejecutarlo sin DOCKER:
> Antes que nada asegurate de tener instalada la version `3.8.10` de `python` y la version `24.0` de `pip`.
Ejecuta los siguientes comandos:
* Instala las dependencias utilizando `pip install -r package-py.txt`.
* Ejecuta la aplicación utilizando `python app.py`.
Aveces los comandos son diferentes y si no te funciona `pip` prueba usando `pip3`, y `python3` en vez de `python`

Una vez hayas ejecutado la aplicacion puedes hacer peticiones al localhost en el puerto 5000, o atravez de swagger.
Para la documentacion de swagger usa el siguiente enlace: [Documentacion de Aplicacion](http://localhost:5000/api/docs/#/)

## Tecnologías Utilizadas
* Python = 3.8.10
* Flask = 3.0.3
* SQLite
