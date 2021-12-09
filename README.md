# Minecraft

## Recursos necesarios para el despligue del servidor

Es necesario que dispongas de los siguientes recursos en tu equipo:
- Linux
- Python 3
- Terraform
- Ansible
- Docker (opcional)
- Servidor FTP remoto (opcional)

## Pasos a seguir

Para desplegar la infraestructura y aprovisionar el servidor, es necesario exportar previamente las siguientes variables de entorno:

# Terraform

## Cloud (Hetzner)

### Conectar con la API de Hetzner

```
export TF_VAR_hcloud_token="<HETZNER-TOKEN>"
```

## Claves SSH pública y privada para la instancia

### Importar clave pública

```
export TF_VAR_ssh_private_key="<SSH-PRIVATE-PATH>"
```

### Importar clave privada

Se puede hacer de dos formas:

1- Utilizando el agente ssh:

```
eval $(ssh-agent)
ssh-add ~/.ssh/minecraft.pk
```

2- Utilizando la clave privada:

```
export TF_VAR_ssh_public_key="<SSH-PUBLIC-PATH>"
```

## DDNS (Dynu)

### Usuario, contraseña y host (previamente creado) de Dynu

```
export TF_VAR_ddns_username="<DYNU-USERNAME>"

export TF_VAR_ddns_password="<DYNU-PASSWORD>"

export TF_VAR_ddns_hostname="<DYNU-URL>"
```

## Instancia

### Hostname de la instancia

```
export TF_VAR_hostname="<SERVER-NAME>"
```

# Ansible

## Clave SSH privada para conectarse a la instancia

Se puede hacer de dos formas:

1- Utilizando el agente ssh:

```
eval $(ssh-agent)
ssh-add <SSH-PRIVATE-PATH>
```

2- Modificando el fichero *ansible/variables.yml*

```
ansible_ssh_private_key_file: <SSH-PRIVATE-PATH>
```

## Variables de entorno

Para modificar las opciones del servidor de Minecraft, hay que modificar las variables de entorno que se encuentran del fichero *ansible/variables.yml* en el apartado de **Minecraf variables**.

# Minecraft

## Mods
Si quieres añadir mods a tu servidor de Minecraft, debes haber configurado previamente el tipo de servidor a *forge* y añadir los ficheros *.jar* en el directorio *files/mods*.

*En este caso, se añade por defecto un fichero de configuración extra para el mod de voz*

Para utilizar los mods en tu cliente debes tener instalado el cliente *forge* y añadir **los mismos** ficheros *.jar* en el directorio *%APPDATA%/.minecraft/mods* de tu equipo.

# Docker

Si quieres probar el servidor en tu equipo local, puedes utilizar el contenedor de Docker que se encuentra en el directorio *docker/minecraft*.

Copia el fichero .env.example del directorio *deployments* a .env y modifica las variables de entorno que se encuentran en el fichero.

```
cp docker/minecraft/deployments/minecraft/.env.example docker/minecraft/deployments/minecraft/.env
```

Una vez tengas todas las variables de entorno correctamente, puedes ejecutar el contenedor de Docker:

```
cd docker/minecraft/deployments
docker-compose up -d
```

## Mods

Para añadir mods en tu servidor local, al igual que en el servidor, debes añadir los ficheros *.jar* a la carpeta *mods* en el directorio *docker/minecraft/data/mods* y reiniciar el contenedor.

```
cd docker/minecraft/deployments
docker-compose restart
```
o
```
docker restart minecraft
```

# Aplicaciones

Una vez tengas todas las variables de entorno configuradas en tu equipo, es nesario crear los ficheros .env para los distintos bots y scripts en python.

## Webserver

Para configurar un pequeño servidor web cuya función es ser una API para obtener información del servidor, es necesario copiar el fichero .env.example del directorio *apps/webserver/app* a .env y modificar las variables de entorno que se encuentran en el fichero.

```
cp apps/webserver/app/.env.example apps/webserver/app/.env
```

### Docker local

Si deseas probar la aplicación en local, es necesario copiar el fichero .env.example del directorio *apps/webserver/deployments* a .env según como quieras configurar el contenedor.

```
cp apps/webserver/deployments/.env.example apps/webserver/deployments/.env
```

Una vez tengas las variables configuradas, puedes lanzarlo con el siguiente comando.

```
cd apps/webserver/deployments
docker-compose up -d
```

Si ya tienes la imagen creada y necesitas modificar las variables del fichero *apps/webserver/app.env*, puedes ejecutar el siguiente comando para volver a construir la imagen:

```
cd apps/webserver/deployments
docker-compose build
```

## Discord bot

Para configurar un bot de Discord para modificar el nombre de un canal según el estado que devuelva la API anterior, es necesario copiar el fichero .env.example del directorio *apps/discord/app* a .env y modificar las variables de entorno que se encuentran en el fichero.

```
cp apps/discord/app/.env.example apps/discord/app/.env
```

Debes tener creados dos canales en Discord (preferiblemente de voz, para que el rol @everyone vea el icono como un candado y no pueda entrar tampoco a escribir) y obtener sus ID, que serán los canales cuyo nombre se modificará según el estado que devuelva la API.

### Docker local

Si deseas probar la aplicación en local, es necesario copiar el fichero .env.example del directorio *apps/discord/deployments* a .env según como quieras configurar el contenedor.

```
cp apps/discord/deployments/.env.example apps/discord/deployments/.env
```

Una vez tengas las variables configuradas, puedes lanzarlo con el siguiente comando.

```
cd apps/discord/deployments
docker-compose up -d
```

Si ya tienes la imagen creada y necesitas modificar las variables del fichero *apps/discord/app.env*, puedes ejecutar el siguiente comando para volver a construir la imagen:

```
cd apps/discord/deployments
docker-compose build
```

# Scripts

## Backup

Si tienes un servidor FTP, puedes configurar el script de backup para compruebe si en dicho servidor hay una carpeta llamada *backup* que contenga una copia anterior de nuestro servidor y tenerlo configurado como estuviese en ese instante.

También se ejecutará cuando se realice un **terraform destroy** para que se haga un backup previo a la destrucción de la infraestructura.

Para que el script funcione, es necesario copiar el fichero .env.example del directorio *scripts/backup* a .env y modificar las variables de entorno que se encuentran en el fichero.

```
cp scripts/backup/.env.example scripts/backup/.env
```

Cuando se ejecute el script, se creará en tu equipo una carpeta llamada *backup* en la raiz de este repositorio en la que almacenará el backup de manera temporal en la transición al servidor FTP.

### Ejecución manual

Este script también puede ser lanzado de forma manual.

Para ello, hay que pasarle como primer argumento 'upload' o 'download'.

```
cd scripts/backup
python backup.py upload
```
```
cd scripts/backup
python backup.py download
```

Si no se indica un segundo parámetro, la ruta desde la que subirá o desde la que descargará el backup será una carpeta llamada *backup* en la raiz del repositorio. En caso de querer utilizar una ruta diferente, puedes especificarla como segundo parámetro.


```
cd scripts/backup
python backup.py upload <path/to/backup>
```
```
cd scripts/backup
python backup.py download <path/to/backup>
```

## Desplegar infraestructura

Una vez hayas realizado todos lo pasos previos, puedes ejecutar el script de despliegue de la infraestructura con el siguiente comando:

Para comprobar como quedará la infraestructura una vez desplegada:
```
cd terraform
terraform plan
```

Y si queremos desplegarla:
```
cd terraform
terraform apply
```

También podemos guardar el plan en un fichero para ejecutarlo y que siempre mantenga el estado de la infraestructura:
```
cd terraform
terraform plan -out <nombre-fichero>
terraform apply <nombre-fichero>
```
