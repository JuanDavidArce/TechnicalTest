
# Prueba técnica

_Este aplicativo permite la gestion de usuarios de diferentes empresas._

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Despliegue** para conocer como desplegar el proyecto.

## Estructura del proyecto

### Pre-requisitos 📋


_Para ejecutar el proyecto debemos tener instalado en nuestro equipo el siguiente software:_

```
Docker:

	-Windows y Mac (https://www.docker.com/products/docker-desktop/)
	
	-Ubuntu: Para instalar docker en este sistema operativo debemos de abrir nuestra termial
	 y escibir los siguientes comandos:
	 
		 * sudo apt update
		 * sudo apt upgrade
		 * sudo apt-get install  curl apt-transport-https ca-certificates software-properties-common
		 * curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
		 * sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
		 * sudo apt update
		 * sudo apt install docker-ce
	
		 Si tienes problemas durante la instalacion puedes visitar:
		 https://www.hostinger.co/tutoriales/como-instalar-y-usar-docker-en-ubuntu 
		 
Docker Compose:

	-Windows y Mac: Este software viene incluido con la instalación de Docker
	
	-Ubuntu: Para realizar la instalación debemos de escribir los siguientes comandos en nuestra terminal:
	
		* sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
		* sudo chmod +x /usr/local/bin/docker-compose
		
		Si tienes problemas con la instalación puedes visitar la siguiente página:
		https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-es 
```

### Instalación y ejecución del proyecto🔧
IMPORTANTE: Debemos abrir la aplicacion de docker en Windows y Mac, una vez hecho esto podemos proseguir con el proceso.
al abrir la aplicacion en windows se podria presentar el error "Hardware assisted virtualization and data execution protection must be enabled in the BIOS", para solucionarlo, basta con abrir una terminal como administrador y correr el comando "bcdedit /set hypervisorlaunchtype auto", reiniciar el pc abrir la aplicacion y continuar con el proceso.

_A continuación se describen los pasos necesarios para tener el proyecto corriendo en nuestro equipo:_

_Para iniciar debemos de descargar el proyecto. Si tenemos git podemos descargar el proyecto fácilmente, entrando a la terminal de nuestro equipo y escribiendo:_

```
-Ubuntu,Windows y Mac:
	* git clone https://github.com/JuanDavidArce/TechnicalTest.git
```

_Si no tenemos git instalado, podemos descargar el archivo comprimido desde la siguiente página:
https://github.com/JuanDavidArce/TechnicalTest.git y una vez descargado descomprimimos el archivo._

_Ya descomprimido el archivo o descargada la carpeta, procedemos a entrar a ella (TechnicalTest), estando dentro, ingresamos a la carpeta accescontrolsystem, una vez allí abrimos una terminal y seguimos con el proceso._

_Tambien podemos movernos hasta dicha carpeta desde una terminal_

_Una vez hecho esto lo primero que vamos a hacer es construir las imágenes y el entorno de Docker necesario para que nuestro proyecto se pueda ejecutar satisfactoriamente, esto lo hacemos con el siguiente comando:_

```
-Windows y Mac:
	* docker-compose build

-Ubuntu:
	* sudo docker-compose build
```

_Una vez construido nuestro entorno vamos a proceder a ejecutarlo con el siguiente comando:_

```
-Windows y Mac:
	* docker-compose up -d

-Ubuntu:
	* sudo docker-compose up -d
```

_Es importante mencionar que debemos crear nuestro usuario root, lo cual lo hacemos moviendonos hasta el sitio donde esta el archivo docker-compose.yml, en nuestra terminal.una vez hecho esto escribimos el siguinete comando *** (role = root) ***:_

```
-Windows y Mac:
	* docker-compose run --rm django python3 manage.py createsuperuser

-Ubuntu:
	* sudo docker-compose run --rm django python3 manage.py createsuperuser
```

_Con el paso anterior ya deberíamos tener nuestro entorno listo para hacer pruebas y verificar el funcionamiento del proyecto lo cual podemos hacer en la direccion *** localhost:8000/users/login/ ***_



## Ejecucion ⚙️

_Una vez hemos creado nuestro usuario root, ya podemos hacer login con el y crear tanto empresas como usuarios para que sean administradores de dichas empresas_

_Cuando hayamos creados usuarios adminstradores y tengamos alguno asignado a una empresa, al correo que se registro van a llegar las credenciales para ingresar a la plataforma_

_Cuando ingresamos con nuestro usuario administrador vamos a tener la opcion de invitar a alguien para que forme parte de la empresa, le llegara un link al correo donde prodra llenar sus datos basicos_

_Ya que tenemos nuestro usuario invitado y registrado, con nuestro usuario administrador podemos crear un punto de acceso al cual le vamos a crear un horario para el usuario que acabamos de registrar_

_Una vez hemos hecho esto ya podemos comenzar a probar nuestra api, lo primero que haremos sera hacer login para obtener el token de acceso y de actualizacion.Enviamos una peticion POST a la ruta *** localhost:8000/api/token/ *** , con un body en formato JSON con los siguientes elementos:_

```
{
	"email":"example@email.com",

	"password":"example password"
}
```

_Con el proceso anterior ya tendriamos nuestros 2 token, el de acceso hay que actualizarlo cada 5 minutos, para hacerlo basta con hacer una peticion POST a la ruta *** localhost:8000/api/toke/refresh/ *** con un Body en formato JSON con los siguientes elementos:_

```
{
	"refresh":"exampletokenrefresh"
}
```

_Finalmente podemos hacer la validacion de acceso para un usuario que se ha registrado mediante el link de invitacion, esto lo hacemos mediante una peticion POST a la ruta *** localhost:8000/api/validate\_access/ *** con un Body en formato JSON con los siguientes elementos_

```
{
	"acces_point_id":Number
}
```

_Es importante mencionar que en esta ultima peticion se requiere que en los headers haya un Key llamado Authorization con un value *** Bearer exampleaccestoken ***_

## Despliegue 📦

_Para hacer deploy es bastante fácil gracias a las facilidades de Docker, para ello solo necesitamos instalar Docker y Docker Compose en nuestro servidor, posterior a esto ejecutar los mismos comandos mencionados en instalación y ejecución, habilitar el puerto en el servidor para que sea accesible, y con esto ya tendríamos nuestra aplicación desplegada._

## Notas



## Construido con 🛠️



* Django/Django Rest Framework- El framework web usado
* Python - Lenguaje de programacion
* Docker - Entorno de trabajo aislado


## Autor✒️


* **Juan David Arce Martinez**



