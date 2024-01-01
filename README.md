# Online Bookstore

## Project Description
This repository is a full-stack online bookshop application offering an intuitive navigation for users to view the product catalog, manage **_CRUD_** operations in the shopping cart, and process online payment through **_PayPal API_**, ensuring secure and reliable transaction environments for users.

## Technical Stack 
The backend of the application is implemented using the framework of **_Python Django_**, with the **_PostgreSQL_** being utilized as the primary database solution for storing the order and user information, **PostgreSQL** comes with more robust features and better performance compared with **SQLite**, the default database embedded into the Django framework.

As for the frontend, I primarily used **_Bootstrap_** for a more modular and easily navigating architecture, **_JavaScript_** and **_AJAX_** were also utilized for ensuring event handling from users clicking on any button and asynchronous communication with backend framework. 

The application was eventually deployed on **_AWS EC2_**, the reason that I selected **EC2** is for the high availability and scalability provided, which fits well with our requirements that the system should be able to scale up and down as the quantity of user requests change. The database was also migrated and hosted on **_AWS RDS_** for fault-tolerant data management as a database deployment strategy. 

* ##### Backend: Django
* ##### Database: PostgreSQL
* ##### Frontend: HTML5, CSS3, JavaScript, AJAX
* ##### Cloud: AWS EC2, S3, RDS, Route 53
* ##### Web Server: Nginx, Gunicorn
