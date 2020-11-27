# python101

Este es un proyecto ejemplo para RockstarG5

##requisitos
-instalar docker
-instalar python 3

##instrucciones
    - Clonar este repo
    - Crear imagen de docker
#### Construir 
docker build -t python101 .
#### correr
docker run -it -p 5000:5000 --rm --name "python101-volatil"
 