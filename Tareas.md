# Tareas

## Tarea 1
###### *Entrega: 12 Junio*
Crear una función que ordene una lista de números.
* Validar que los elementos de la lista sean números
* Usar como parámetro una lista
* Regresar la lista ordenada

## Tarea 2
###### *Entrega: 15 de Junio**
Con expresiones regulares realizar las siguientes validaciones:
* Correo electrónico:
    * Dominio + 1 extension: *Ej. juan@padts.mx*
    * Dominio + 2 extensiones: *Ej. juan@padts.com.mx*
    * Subdominio + dominio + extensión: *Ej. juan@python.padts.mx*
* Número telefónico:
    * 10 dígitos: *Ej. 3314567822*
    * Lada indicada en parentésis (2 0 3 números): *Ej. (33)14567822, (331)4567822*
        * Pueden existir espacios o guines como separador: *Ej. (33) 1456 7822, (331) 456-7822*
        * EXTRA: Los separadores deben ser iguales

[*] La fecha se extiende al 19 de Junio por la configuración de los repositorios

## Tarea 3
###### *Entreaga: 23 de Junio*
La **Tarea 3** consiste en emular en funcionamiento de una base de datos utilizando Pickle y Shelve cumpliendo con los siguientes puntos
* Crear 5 objetos estudiante (utilizando clase creada en el `Ejercicio 3`)
* Crear una función para guardar estudiantes.
* Crear una función para leer estudiantes.
* Crear una función para actualizar estudiantes.
* Crear un Modulo llamado StudentIO que contenga las funciones.

Las funciones se deben crear tanto para Pickle como para Shelve.


## Tarea 4
###### *Entrega: 26 de Junio*
Replicar `Tarea 3` utilizando base de datos con *Mongo Engine*
* Se debe crear un modelo de estudiante que herede de *Document*
* Utilizar base de datos con nombre 'padts' y coleccion 'estudiantes'
* Crear método para escritura
    * Se debe ingresar los datos de estudiante como un objeto del modelo.
* Crear método para lectura
    * Se debe indicar el estudiante por parámetro
    * Se debe regresar un objeto del modelo de estudiante
* Crear método para actualización
    * Se debe indicar el estudiante por parámetro
    * Se debe retornar el estudiante actualizado
* Crear método para eliminar
    * Se debe indicar el estudiante por parámetro
    * Se debe retornar un objeto con todos los estudiantes restantes

 
