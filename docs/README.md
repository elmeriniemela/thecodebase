## The Codebase

Funtionality:
* Integration with github to make a portfolio website based on projects.
* JavaScript games.


Install & Run:
* https://docs.docker.com/engine/install/ubuntu/
* https://docs.docker.com/compose/install/
* `cp thecodebase.env-example thecodebase.env`
* `docker-compose up --build`

Setup database:
* `docker-compose exec thecodebase python manage.py migrate`
* `docker-compose exec thecodebase python manage.py createsuperuser`

Notes:
* All `docker-compose` commands should be ran on the root directory of this repo.
* For `DEBUG=0` you need nginx, see `example-nginx.conf`
* To access the container run `docker-compose exec thecodebase bash`

Python PDB:
* Enable `stdin_open: true` and `tty: true` on docker-compose.yml
* Add breakpoint `import pdb; pdb.set_trace()`
* Attach to container `docker attach thecodebase-thecodebase_1`
* Detach with `Ctrl + P, Ctrl + Q`

![alt text](https://raw.githubusercontent.com/elmeriniemela/thecodebase/master/docs/thecodebase.png)

