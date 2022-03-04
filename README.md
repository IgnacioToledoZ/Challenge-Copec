# Challenge-Copec

¡Hola a todos, espero que se encuentren bien!
En este escrito les comento como ejecutar el código que realicé para este challenge que se me entregó, espero que cumpla el objetivo.

## Para comenzar
En primer lugar, todos los archivos relacionados con el código están publicados en este repositorio de github. 
Luego se debe abrir el archivo app.py desde el terminal de un IDE de Python. Yo ocupé PyCharm. Se debe teclear el siguiente código en el terminal:

```py
python app.py
```

Con esto, la aplicación está funcionando, específicamente en el puerto 5000 del local host.
Se añadió un archivo con usuarios que el programa precarga al empezar a funcionar,llamado usuarios.py, pero solo es para tener algo en un archivo y poder mostrarlo.


Para la petición HTTP GET, podemos entrar a un navegador web como Google Chrome y escribir el siguiente texto para poder obtener los usuarios:

```http
http://localhost:5000/usuarios

```

Lo anterior solo nos muestra los usuarios precargados en un archivo, y estos se encuentran en formato JSON.

## Framework para casos de uso

El framework utilizado fue Flask.

## Casos de uso

Para poder probar los casos de uso, se ocupó la el programa Insomnia que es un REST API Client que permite generar peticiones HTTP (GET, POST, PUT & DELETE), por lo que sugiero ocupar esta u otra aplicación para poder corroborar las funcionalidades.

### Petición **POST**

Para poder registrar nuevos usuarios realizamos una petición POST y entregamos un objeto en formato JSON para poder ser ingresado, dando los datos de nombre, apellido, email y fecha de nacimiento. 
La ruta debe ser la siguiente:

```http
http://localhost:5000/usuarios

```


La petición debe ser de la siguiente forma:

```js
{
"nombre":"felipito",
	"apellido": "munoz",
	"email": "fmunoz@uc.cl",
	"fecha_nacim": "1942-03-15"
}
```

La petición anterior nos entrega lo siguiente:

```js
{
	"message": "200 OK - Usuario añadido con éxito",
	"usuarios": [
		{
			"apellido": "toledo",
			"email": "iptoledo@uc.cl",
			"fecha_nacim": "1997-12-09",
			"id": 1,
			"nombre": "ignacio"
		},
		{
			"apellido": "perez",
			"email": "pperez@uc.cl",
			"fecha_nacim": "1999-06-10",
			"id": 2,
			"nombre": "pedrito"
		},
		{
			"apellido": "gonzalez",
			"email": "jgonzalez@uc.cl",
			"fecha_nacim": "1996-07-28",
			"id": 3,
			"nombre": "juan"
		},
		{
			"apellido": "munoz",
			"email": "fmunoz@uc.cl",
			"fecha_nacim": "Sun, 15 Mar 1942 00:00:00 GMT",
			"id": "4ca23009-29d3-4d62-80b5-e0644e44c78a",
			"nombre": "felipito"
		}
	]
}
```

Como se puede ver, la creación de un usuario le entrega un id en formato UUID4 (random), además de verificar el formato de la fecha de nacimiento (YYYY-MM-DD) y el formato de mail (name@example.xxx).


### Petición **PUT**

Para actualizar los datos de un usuario generamos una petición PUT a la ruta con el nombre del usuario a cambiar, de la forma siguiente:

```http
http://localhost:5000/usuarios/felipito

```
La petición debe tener un cambio en sus datos para que tenga sentido, y es de la forma JSON, como sigue:
```js
{
"nombre":"felipitooo",
	"apellido": "munozzzzz",
	"email": "fmunoz@uc.cl",
	"fecha_nacim": "1942-03-15"
}
```

Lo que nos entrega la siguiente respuesta:

```js

{
	"message": "200 OK - Usuario actualizado con éxito",
	"usuario modificado": {
		"apellido": "munozzzzz",
		"email": "fmunoz@uc.cl",
		"fecha_nacim": "Sun, 15 Mar 1942 00:00:00 GMT",
		"id": "4ca23009-29d3-4d62-80b5-e0644e44c78a",
		"nombre": "felipitooo"
	},
	"usuarios": [
		{
			"apellido": "toledo",
			"email": "iptoledo@uc.cl",
			"fecha_nacim": "1997-12-09",
			"id": 1,
			"nombre": "ignacio"
		},
		{
			"apellido": "perez",
			"email": "pperez@uc.cl",
			"fecha_nacim": "1999-06-10",
			"id": 2,
			"nombre": "pedrito"
		},
		{
			"apellido": "gonzalez",
			"email": "jgonzalez@uc.cl",
			"fecha_nacim": "1996-07-28",
			"id": 3,
			"nombre": "juan"
		},
		{
			"apellido": "munozzzzz",
			"email": "fmunoz@uc.cl",
			"fecha_nacim": "Sun, 15 Mar 1942 00:00:00 GMT",
			"id": "4ca23009-29d3-4d62-80b5-e0644e44c78a",
			"nombre": "felipitooo"
		}
	]
}

```

También nos aseguramos de que los datos actualizados cumplan los requisitos (email y fecha de nacimiento).

### Petición GET

Para obtener un usuario en base a su id, necesitamos generar una petición GET, con la siguiente ruta y utilizando el id correspondiente:

```http
http://localhost:5000/usuarios/4ca23009-29d3-4d62-80b5-e0644e44c78a

```
La respuesta es la siguiente:

```js

{
	"message": "200 OK",
	"usuario": {
		"apellido": "munozzzzz",
		"email": "fmunoz@uc.cl",
		"fecha_nacim": "Sun, 15 Mar 1942 00:00:00 GMT",
		"id": "4ca23009-29d3-4d62-80b5-e0644e44c78a",
		"nombre": "felipitooo"
	}
}
```

### Petición DELETE

Para eliminar un usuario en base a su id, es necesario realizar una petición DELETE utilizando la siguiente ruta y utilizando el id correspondiente:


```http
http://localhost:5000/usuarios/4ca23009-29d3-4d62-80b5-e0644e44c78a

```
La respuesta es la siguiente:

```js
{
	"message": "200 OK - Usuario Eliminado",
	"usuarios": [
		{
			"apellido": "toledo",
			"email": "iptoledo@uc.cl",
			"fecha_nacim": "1997-12-09",
			"id": 1,
			"nombre": "ignacio"
		},
		{
			"apellido": "perez",
			"email": "pperez@uc.cl",
			"fecha_nacim": "1999-06-10",
			"id": 2,
			"nombre": "pedrito"
		},
		{
			"apellido": "gonzalez",
			"email": "jgonzalez@uc.cl",
			"fecha_nacim": "1996-07-28",
			"id": 3,
			"nombre": "juan"
		}
	]
}
```


## Saludos

Espero que este Challenge haya podido ser respondido a cabalidad. Saludos y espero nos veamos pronto.






