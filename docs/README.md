# The Codebase


[www.thecodebase.site](http://www.thecodebase.site "www.thecodebase.site")


![alt text](https://raw.githubusercontent.com/thecodebasesite/django_thecodebase/master/docs/thecodebase.png)

Install instructions:

* `sudo apt install libpq-dev -y`
* `git clone <this repo>`
* `cd <this repo>`
* `virtualenv -p python3.6 /home/elmeri/.venv/django`
* `source /home/elmeri/.venv/bin/activate`
* `pip install -r requirements.txt`
* `createdb thecodebase`
* `python manage.py migrate`
* `python manage.py runserver`
