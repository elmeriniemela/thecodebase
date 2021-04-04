## The Codebase

Funtionality:
* Integration with github to make a portfolio website based on projects.
* JavaScript games.


Install instructions:
* `docker-compose up --build`

Setup database:
* `docker-compose exec app python manage.py migrate`
* `docker-compose exec app python manage.py createsuperuser`
* `docker-compose exec app python manage.py collectstatic --noinput`


![alt text](https://raw.githubusercontent.com/elmeriniemela/thecodebase/master/docs/thecodebase.png)

