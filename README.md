# tiendamusicalMVC
Tienda Musical con CRUD en patrón MVC utilizando POO

Gebhard Records’ CRUD App:
¡La discográfica Gebhard Records™ se enorgullece de que haya elegido nuestros servicios! Nuestra aplicación de CRUD le permitirá un correcto manejo de registros y consultas sobre sus artistas y álbumes favoritos.

Instalación:
La aplicación es de fácil instalación: basta con descargar nuestro archivo:  
tiendamusicalMVC.zip               
extraerlo y ejecutar el archivo: controlador.py desde un editor de código 
Los editores que pueden utilizarse incluyen –pero no están limitados a- Visual Studio Code, JupyterLab, IDLE, etc.

Características:
Nuestra aplicación considera 4 campos: artista, álbum, unidades y valor. 
La misma permite funciones CRUD/ABMC: dar de alta y de baja elementos, consultar los valores hasta el momento 
y permite la modificación de los mismos. Los datos colocados son guardados dentro de una base de datos que utiliza SQLite. 
Su entorno gráfico está realizado mediante el uso de Tkinter.

Contribución:
GitHub: https://github.com/ceciliagebhard/tiendamusicalMVC.git
Las pull requests son bienvenidas: ante la necesidad de modificar el código preexistente, abra un issue en GitHub postulando qué desea cambiar. 

Implementación de Regex:
Se encuentra en la rutina que define el “Alta” en la fila 49 del script del archivo modelo.py
patron = "[a-zA-Záéíóú 0-9 \s]+" #regex que valida campo de entrada artistas tolerando varios espacios, entre caracteres alfanúmericos.

Implementación de Excepciones: 

1era Excepción: Se encuentra el uso de try/except/finally en el constructor __init__ en las filas 15, 28 y 30 (respectivamente) del script del archivo modelo.py #excepción que comunica que la base de datos se crea al dar el alta, y en caso de estar creada da otro aviso.
#mediante finally, en ambos casos comunica que se puede consultar, modificar o eliminar.

2da Excepción: Se encuentra el uso de raise en la rutina que define el "Alta" en la fila 51 del script del archivo modelo.py #excepción que impide el alta si se ingresa un número negativo en el item unidades

Integrantes del grupo:
Matias Estigarribia, Cecilia Gebhard, Emilio Herrera, Diego Jordan e Ignacio Lopez Habiague.


Soporte:
En caso de encontrarse con dificultades en la instalación o funcionamiento de nuestra aplicación, no dude en contactar con nosotros.

Licencia:
El Proyecto está bajo licencia de Gebhard Records™.
