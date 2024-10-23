# API AGENDA

## 1 - script con las siguientes caracteristicas:
### 1.1 crear la base de datos db_agenda
### 1.2 crear la tabla personas
### 1.3 insertar 3 registros

## 2 - configurar el respositorio con los siguientes elementos:
### 2.1 README.md
### 2.2 LICENSE
### 2.3 requirements.txt (fastapi)
### 2.4 .gitignore

## 3 - instalar mysql
````bash
sudo apt-get update
sudo apt-get install mysql-server -y
````
## 4 - iniciar sesion en el servidor
````bash
sudo service mysql start
````
## 5 - Actualizar el repositorio
````bash 
sudo apt-get update
````
## 6 - Configurar la contraseña de root 
````bash
sudo mysql_secure_installation
````
## 7 - Acceder a MySQL 
```` bash
sudo mysql -u root -p
````