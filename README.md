# Online Bookstore

## Project Description
This repository is a full-stack online bookshop application offering an intuitive navigation for users to view the product catalog, manage **_CRUD_** operations in the shopping cart, and process online payment through **_PayPal API_**, ensuring secure and reliable transaction environments for users.

## Technical Stack 
The backend of the application is implemented using the framework of **_Python Django_**, with the **_PostgreSQL_** being utilized as the primary database solution for storing the order and user information, **PostgreSQL** comes with more robust features and better performance compared with **SQLite**, the default database embedded into the Django framework.

As for the frontend, I primarily used **_Bootstrap_** for a more modular and easily navigating architecture, **_JavaScript_** and **_AJAX_** were also utilized for ensuring event handling from users clicking on any button and asynchronous communication with backend framework. 

The application was eventually deployed on **_AWS EC2_**, the reason that I selected **EC2** is for the high availability and scalability provided, which fits well with our requirements that the system should be able to scale up and down as the quantity of user requests change. The database was also migrated and hosted on **_AWS RDS_** for fault-tolerant data management as a database deployment strategy. 

## Why NGINX and Gunicorn?
**Gunicorn** is a web server, written completely in Python. It can run as a standalone server and handle clients requests directly (including serving static files). However, using it this way is highly inefficient, mainly because Python itself is slow. That’s where **NGINX** comes into the picture.

**NGINX** is written in C which means that it is very fast, but **NGINX** can’t run Python programs, it can only serve static files, So, the usual scenario is letting **NGINX** serve static files (the task where **NGINX** shines) and forward all dynamic requests (the ones that are expected to be handled by your Django app) to **Gunicorn**. In this situation, **NGINX** acts as a reverse proxy for a **Gunicorn** server, passing all dynamic requests to **Gunicorn**, and as a regular server for static files, handling this task on its own. So, the requests for static files never reach **Gunicorn** server.

Besides, serving static assets, **NGINX** can also cache the responses from Gunicorn in the filesystem, which means that any future requests to the same URL are treated as static requests — this means that those requests will never reach **Gunicorn** and be handled completely by **NGINX**. This in turn means that a website will have a much higher performance, because we are able to skip the weakest point in the infrastructure — **Gunicorn** and use the fastest program to serve the data.

#### Check out more information from here: [Why use NGINX and Gunicorn](https://medium.com/@HannahMel/nginx-gunicorn-and-wsgi-e1795943536e#:~:text=It%20can%20handle%20them%20very,code%20is%20executed%20when%20needed.)

## NGINX and Gunicorn running status
![gunicorn](https://github.com/weizihan1213/Online-Bookstore/blob/main/gunicorn_status.png)

![nginx](https://github.com/weizihan1213/Online-Bookstore/blob/main/nginx_status.png)

* ##### Backend: Django
* ##### Database: PostgreSQL
* ##### Frontend: HTML5, CSS3, JavaScript, AJAX
* ##### Cloud: AWS EC2, S3, RDS, Route 53
* ##### Web Server: Nginx, Gunicorn
