[![Build Status](https://travis-ci.com/fitplusplus/fithub.svg?branch=master)](https://travis-ci.com/fitplusplus/fithub)

# Fithub

## Descripción

Problema a resolver: queremos crear una herramiento para crear workouts personalizados basados en la elección de grupo muscular, número de repeticiones, intensidad o tipo de entrenamiento.

Solución propuesta: crear una interfaz CLI y una pequeña base de datos con ejercicios. El usuario especificará los parámetros deseados para crear su workout, y este aparecerá como una cadena de texto en la terminal.

## Herramientas

La elección de la siguiente lista la discutimos [aquí](https://github.com/fitplusplus/fithub/issues/7)

- Lenguaje: `Python`
- Logging: módulo `logging` de `Python` (localmente) y PaperTrails o LogDNA (servidor)
- Servicio de configuración remota: `etcd`.
- Base de datos: MongoDB al principio, posiblemente PostgreSQL en el futuro.

## Estructura del proyecto

- En la carpeta [src](src/) se encuentra el código del proyecto.

## Contribuidores

| Nombre  | Nick          | Correo                    |
| ------- | ------------- | ------------------------- |
| Elena   | @elenamerelo  | elenamerelo@correo.ugr.es |
| Antonio | @antoniogamiz | antoniogamiz10@gmail.com  |

# Instrucciones

Para instalar las dependencias:

	poetry install

Para ejecutar los tests:

	poetry run poe test

