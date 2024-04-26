# ProyectoFinal

Bienvenidos a mi proyecto final de python realizado en coderhouse.

En este proyecto trabaje sobre un prototipo de blog, el cual hace referencia a mi idolo Lionel Andres Messi.

# En el primer paso, para extraer el proyecto es necesario usar Git, abrir terminal dentro de Visual Studio y ejecutar

git init enter

git clone + el link de este repositorio, enter.

# En el segundo paso tenemos que ejecutar cd .\messi_blog\ para posicionarnos sobre la carpeta del blog y despues de eso, si

podemos ejecutar python manage.py runserver para iniciar el proyecto.

# En el tercer paso debemos copiar la direccion brinddad por la consola de python (http://127.0.0.1:8000/) o posicionarnos sobre la

direccion y presionar la tecla ctrl + click izquierdo.

######################################
Usuarios de prueba admin y prueba

El user admin es el super usuario.

datos de logueo
user: prueba
password: messi1987

#####################################

El proyecto se basa completamente en el modelo trabajado en clase MVT (Model, view, template) el cual como base usamos una 

plantilla descargada en bootstrap la cual, modifique a mi gusto.

La pagina principal del proyecto contiene un menu con login, registro, 4 link "home" (hay estar logueado para ir a esa vista),

"about" (te cuento un poquito de mi), "posteos" y "sitio oficial" (redirecciona a la pagina oficial de Messi).

En las vistas de login y registro se encuentran los formularios respectivos para poder ingresar y registrarte.

Una vez registrado y logueado en la seccion posteos vas a encontrar el mensaje de bienvenida, el boton perfil (para editar el mismo) y el boton cerrar sesion, ademas de la vista en miniatura de los posteos creados, y un boton para crear el nuevo posteo.

Dentro del posteo vas a poder editar y eliminarlo, dentro del perfil vas a poder ver el nombre apellido e email con el cual te registraste. Tambien vas a poder agregar un avatar presionando el boton "editar perfil".

