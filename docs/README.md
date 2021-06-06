## The Codebase

Funtionality:
* Integration with github to make a portfolio website based on projects.
* JavaScript games.


Install & Run:
* https://docs.docker.com/engine/install/ubuntu/
* https://docs.docker.com/compose/install/
* `$ cp docs/thecodebase.env-example thecodebase.env`
* `$ docker-compose build --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) --build-arg USERNAME=$USER`
* `$ docker-compose up`

Setup database:
* `$ createdb thecodebase`
* `$ docker-compose exec thecodebase python manage.py migrate`
* `$ docker-compose exec thecodebase python manage.py createsuperuser`

Service:
* `# cp docs/thecodebase.service-example /etc/systemd/system/thecodebase.service`
* `# systemctl enable thecodebase.service --now`


Python PDB:
* Enable `stdin_open: true` and `tty: true` on docker-compose.yml
* Add breakpoint `import pdb; pdb.set_trace()`
* Attach to container `docker attach thecodebase-thecodebase_1`
* Detach with `Ctrl + P, Ctrl + Q`

Notes:
* All `docker-compose` commands should be ran on the root directory of this repo.
* For `DEBUG=0` you need nginx, see `example-nginx.conf`
* To access the container run `docker-compose exec thecodebase bash`

![alt text](https://raw.githubusercontent.com/elmeriniemela/thecodebase/master/docs/thecodebase.png)

