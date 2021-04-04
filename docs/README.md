## The Codebase

Funtionality:
* Integration with github to make a portfolio website based on projects.
* JavaScript games.


Install & Run:
* `docker-compose up --build`

Setup database:
* `docker-compose exec app python manage.py migrate`
* `docker-compose exec app python manage.py createsuperuser`

Notes:
* All `docker-compose` commands should be ran on the root directory of this repo.
* For `DEBUG=0` you need nginx, see `example-nginx.con`
* To access the container run `docker-compose exec app bash`


![alt text](https://raw.githubusercontent.com/elmeriniemela/thecodebase/master/docs/thecodebase.png)

