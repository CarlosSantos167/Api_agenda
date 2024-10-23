# Fast_API_Groq

## 0. Actualizar la lista de versiones de las librerias del sitema operativo

Actualiza la lista de versiones de las librerias del sitema operativo.

````shell
sudo apt update
````
## 1. Instalar neofetch

Instalar neofetch para conocer las caracteristica del sistema operativo que se esta usando

````bash
sudo apt install neofetch -y
````
## 2. Ejecutar neofetch

Ejecutar neofetch

````bash
neofetch
````
Nota: crear el archivo OS.txt con la version del sistema
## 3. crear un ambiente virtual

````shell
virtualenv venv
````

## 4. Entrar al ambiente virtual

iniciar el ambiente virtual

````bash
source venv/bin/activate
````

## 5. salir del ambiente virtual

descartivar el ambiente virtual

````bash
deactivate
````

## 6. crear el archivo .gitignore

crear el archivo .gitignore

````bash
*.pyc
__pycache__/
venv/
````
## 7. instalar las libreria nesesarias

para este pryecto se usaran las librerias de [FastAPI](https://fastapi.tiangolo.com/)
````bash
pip install "fastapi[standard]"
````

## 8. crear el archivo requirements.txt

se genera el archivo requirements.txt para listaar las librerias necesarias para el proyecto y sus versiones

````bash
pip freeze > requirements.txt
````
## 9. crear el archivo runtime

crear el archivo runtime con la version de python que se esta utilizando

````bash
python3 -V > runtime
````
## 10. Indexar los archivos creados con git

````bash
git add. 
git commit -m (nombre)
git push -u origin main
````