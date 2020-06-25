# Ejercicios

## Ejercicio 1: *Condicionales*
###### *9 Junio*
Elaborar los siguientes ejercicios:
* Validar si un número es positivo, negativo o cero.
* Validar si un número es par o impar.
* Validar si un número es primo.
* Escribir una función que con las validaciones anteriores.
* Validar si un año es bisiesto (escribir función)

## Ejercicio 2: *Regex*
###### *10 de Junio*
Definir patrones para cadenas de texto que:
* No yenga letras
* Solo tenga números
* Solo tenga letras mayúsculas
* Solo tenga letras minúsculas
* No tenga numeros

## Ejercicio 3: *POO*
###### *11 de Junio*
Ejercicios para prácticar las propiedades de la programación orientada a objetos
* Herencia y polimorfismo:
    * Definir una clase Figura con atributos y métodos.
    * Definir una clase rectángulo que hereda de figura.
    * Definir una clase Triángulo que hereda de figura.
 
 
* Encapsulación 
    * Crear una clase estudiante son atributos: nombre, correo electrónico y contraseña.
    * Crear métodos para ingresar y obtener los atributos.
 
 
## Ejercicio 4: Clientes y servidores
###### *22 de Junio*
Crear clases para clientes y servidores TCP y UDP.
* Crear una clase para cliente TCP
    * Dede realizar la conexión en el constructor
    * Debe tener un método para escribir con un parámetro para el mensaje
    * Debe tener un método para leer que retorne el mensaje


* Crear una clase para servidor TCP [*, **]
    * Debe asignar puerto en el constructor
    * El constructor contiene el procedimiento para aceptar las conexiones
    * Debe tener un método para escribir con un parémetro para el mensaje
    * Debe tener un método para leer que retorne el mensaje
    
* Crear una clase para cliente UDP
    * Debe tener un método para escribir con un parametro para el mensaje y otro con la dirección (ip + puerto)
    * Debe tener un método para leer que retorne el mensaje y la dirección (ip + puerto)
    
* Crear una clase para servidor UDP [*, **]
    * Debe asignar puerto en el constructor
    * El constructor contiene el procedimiento para recibir paquetes
    * Debe tener un método para escribir con un parámetro para el mensaje y otro con las dirección (ip +puerto)
    * Debe tener un método para leer que retorne el mensaje y la dirección (ip + puerto)
    
    
\* Los servidores deben implementar un procedimiento de salida del loop

\** No se limita el número de paquetes


## Ejercicio 4: Servidor Multiples Clientes
###### *24 de Junio*
Crear un servidor TCP o UDP para atender a múltiples clientes al mismo tiempo
* Se debe indicar el tipo de servidor
* El servidor debe mostrar mensaje en consola cuando reciba un mensaje
* El servidor debe responder cada paquete que reciba
* El servidor debe llevar conteo de paquetes por cliente
* Definir mecanismo de salida 