## The Codebase

Funtionality:
* Integration with github to make a portfolio website based on projects.
* JavaScript games.


Install instructions:

* `docker build -t .`
* `docker-compose up`

Setup database:
* `pip install -r requirements.txt`
* `createdb thecodebase`
* `python manage.py migrate`
* `python manage.py createsuperuser`
* `python manage.py runserver`


![alt text](https://raw.githubusercontent.com/elmeriniemela/thecodebase/master/docs/thecodebase.png)

