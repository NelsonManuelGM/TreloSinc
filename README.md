************
TreloSinc Demo
************
Django app to synchronize with trello.com

This project use django, django-rest-framework, PostgreSQL and Docker

#Database Server

##### Install database using docker-compose.

    >> cd /path/to/root/directory
    >> sudo docker-compose up db

#Application Server

##### Move to application root directory
    >> cd /path/to/root/directory

##### Create python virtualenv in linux console
    >> virtualenv venv

##### Activate created virtualenv
    >> source venv/bin/activate

##### Install | Run app with docker-compose
    >> sudo docker-compose up web

The application will run on the url http://127.0.0.1:8000

#API Documentation

##### Main endpoints

* To synchronize with Trello.com: GET -> http://127.0.0.1:8000/trello_sinc/
* To get all synchronized boards: GET -> http://127.0.0.1:8000/boards
* To get all synchronized cards: GET -> http://127.0.0.1:8000/cards
* To get all synchronized cards by board id: GET -> http://127.0.0.1:8000/cards?board_id={board_id} 
using the query param board_id.

##### Auxiliary endpoint

* To delete all synchronized data: DELETE -> http://127.0.0.1:8000/boards

*Port would be different if default configuration is changed or the 8000 port is busy*

#TEST
####

Execute:

    >> python manage.py test
