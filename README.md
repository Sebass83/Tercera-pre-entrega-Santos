<p align="center">
  <a href="https://www.coderhouse.com/" target="blank"><img src="https://www.coderhouse.com/imgs/ch.svg" width= "400" alt="Nest Logo" /></a>
</p>

<p align="center">
  <a href="https://www.python.org/" target="blank"><img src="https://www.python.org/static/img/python-logo.png" width="200" alt="Nest Logo" /></a>
</p>

# CoderHouse
## Tercera pre-entrega Sebastian Santos

### Objetivos generales:
✅ Desarrollar una WEB Django con patrón MVT subida a Github.

### Se debe entregar:

✅ Link de GitHub con el proyecto totalmente subido a la plataforma.

✅ Proyecto Web Django con patrón MVT que incluya:
1. Herencia de HTML.
2. Por lo menos 3 clases en models.
3. Un formulario para insertar datos a todas las clases de tu models.
4. Un formulario para buscar algo en la BD
5. Readme que indique el orden en el que se prueban las cosas y/o 
donde están las funcionalidades.

### Formato:

✅ Link al repositorio de GitHub con el nombre “Tercera pre-entrega+Apellido”.

### Sugerencias:

✅ Activar comentarios en el archivo y usar como guía el proyecto subido al material complementario de esta clase. También pueden obtener la rama de Git que tiene el mismo material Rama-De-Git.


# Para ejecutar la APP:

1. ###  Si no tiene instalado Django, instálelo:
```
pip install django
```
2. ###  Correr las migraciones de la Base de datos:
```
python manage.py migrate
```
3. ###  Ejecutar la aplicación:
```
python manage.py runserver
```

# Como funciona la aplicación:

```TercerPreEntrega``` es la proyecto y en el se encuentra el punto de entrada mediante su archivo ```urls.py```.
```urls.py``` no solo muestra las urls de ```TercerPreEntrega```, a su vez incluye las de ```CoderBlogApp```

La aplicación ```CoderBlogApp``` implementa MVT(Model - View - Template), en esta nos encontraremos con los siguientes apartados a tratar:

## 1. models.py:

Aquí se encuentran los ```Modelos``` que se utilizaran para persistir los datos en la base de datos.
### BlogSummary:

>```title```

>```description```

>```author```

>```entryDate```

>```min_img_url```

### Blog:

>```post```

>```hero_img_url```

>```quote```

>```acent_img_url```

### EntryBlogData

>```author```

>```entryDate```

>```slug```

## 2. urls.py:

Punto de entrada para las urls correspondientes a ```CoderBlogApp```


## 3. Templates:
>### 1. base.html.
Este se usa para la ```herencia de HTML``` es el template base.
El mismo se encuentra separado en tres partes:

1. nav:
   > Aquí encontraran  el "Logo", la Navegación y el Formulario para la búsqueda, este ultimo busca por ```title``` en la base de datos y retorna el post con ```title```
2. block main
   > Bloque de entrada dinámica.
3. footer
   > Pie de pagina.
>### 2. inicio.html. 
 >ingresa la estructura al bloque dinámico lo necesario para mostrar en la ```vista```, específicamente la estructura HTML y el JS para poder dar función a las tarjetas.


>### 3. post.html.
  >ingresa la estructura al bloque dinámico lo necesario para mostrar en la ```vista```
  , específicamente la estructura HTML para poder ver un post en particular.


>### 4. crear_post.html.
  >ingresa la estructura al bloque dinámico lo necesario para mostrar en la ```vista```, específicamente el formulario para crear nuevos post.


## 4. Vistas:
Consta de tres funciones usando los ```helpers``` son los encargados de retornar cada vista.

1. ```inicio``` usando ```helperGetAllPosts``` obtiene todos los post y los muestra en la vista.
2. ```crear_post``` usando ```helperNewPost``` mediante el formulario que se encuentra en la vista persiste el nuevo post en la base de datos
3. ```post``` usando ```helperPostRequest``` es es el encargado de mostrar en la vista un post en particular, ya sea si este viene desde la búsqueda realizada mediante el formulario o si viene por hacer click en una card

## 5. Helpers
```helperGetAllPosts```:

>```helperGetAllPosts``` es la función encargada de realizar las búsquedas según un termino dado.

### El Termino de búsqueda puede tener dos orígenes distintos:

>1- Este viene desde el formulario de búsqueda que se encuentra 
en el template base, en este caso solo busca por titulo.

>2- Este viene desde las card del inicio, gracias al cards.js.
Al hacer click en la card utiliza el atributo data en la misma 
y redirige a la locación de busque usando como termino el atributo 
data anteponiendo un "@"

>Si el termino de busque comienza con "@" el código asume que se esta
buscando por slug, hace la búsqueda y retorna los resultados.

>Si el termino de busque no comienza con "@" el código asume que se esta
buscando por title, hace la búsqueda y retorna los resultados.


```helperNewPost```:
>```helperNewPost``` es el encargado de persistir la data en la db para los siguientes modelos:

>```BlogSummary```:
  
  > title

  > description
  
  > author
  
  > entryDate
  
  > min_img_url

>```Blog```:

  >post

  >hero_img_url
  
  >quote
  
  >acent_img_url

>```EntryBlogData```:
  
  >author
  
  >entryDate
  
  >slug

```helperPostRequest```
```helperGetAllPosts``` es la función encargada de traer todo lo necesario para mostrar la vista inicio mediante su correspondiente template, esta trae todos los datos necesarios desde la base de datos.





