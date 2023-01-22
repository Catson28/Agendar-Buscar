# Informacoes relevantes.


## Criar o projecto com o django  

#### Primeiro criamos a pasta e posteriormente abrimos a mesma com o VS code que ee o nosso caso

    mkdir 'schedule-calendar'    
    cd 'schedule-calendar' 
    code . 

####  Abrimos um novo terminal e instalamos o Ambiente virtual e iniciamos o nosso projecto django e aplicacao

    virtualenv env  
    source env/bin/activate 

	pip install django==4.1.1
	django-admin.py startproject core .
	python manage.py startapp shedulle

#### instalar a aplicacao no projecto por intermedio do ficheiro

- `settings.py`

#### Criamos um ficheiro para as dependencias que serao instaladas
`requirements.txt` efectuamos as alteracoes na model e rodamos os comandos abaixo para criar o banco de dados

	python manage.py migrate
	python manage.py runserver
    pip install -r requirements.txt  
	pip install djangorestframework

#### cria um super usuario, para acessar a base de dados atravez da rota admin

	python manage.py createsuperuser

#### Inicializamos o repositorio remoto do github

	git init
	git add .
	git commit -m "Criacao do projecto"
	git branch -M main
	git remote add origin https://github.com/Catson28/Agendar-Buscar.git
	git push -u origin main

#### Colocamos a aplicacao a rodar
    python manage.py runserver   




## **DATABASE**


### **TABLES REFERRING TO THE BUSINESS**

**Package**
-   name
-   price
    
**Album**
-   type
-   number of photos
-   price
-   size
    
**Frames**
-   type
-   size
-   price
    
**Photography**
-   type
-   size
-   price

**Pen_drive**
-   type
-   capacity
-   price
    
**Video**
-   type
-   duration
-   format
-   price
    
**Professionals**
-   the_area
-   office

**Interested**
-   name
-   source(social media)
   
**Professionals**
-   area
-   office
    


**Celebrants**
-   name
-   contact
 
**Client**
-   name
-   contact
    
**Place**
-   Name
-   address
-   contact

**Schedule**
-   action
-   start date
-   end date
-   icom
   
**Candstudio_Schedule**
-   idAgenda
-   idPackage
-   idClient
   
**Candstudio_Schedule_****C****elebrants**(see all children)
-   idAgendCand
-   idCelebrants
    
### **TABLES REFERRING TO THE CONTENTS**

**Subject_matter**
-   title
-   definition
    
**Post**
-   title
-   Definition
    
**Image**
-   name
    
**Text**
-   title
-   description