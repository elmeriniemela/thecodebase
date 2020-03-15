# The Codebase


[www.thecodebase.tech](http://www.thecodebase.tech "www.thecodebase.tech")


![alt text](https://raw.githubusercontent.com/thecodebasesite/thecodebase/master/docs/thecodebase.png)

Install instructions:

* `sudo apt install libpq-dev -y`
* `git clone <this repo>`
* `cd <this repo>`
* `mkdir ~/.venv`
* `virtualenv -p python3.6 ~/.venv/django`
* `source ~/.venv/bin/activate`
* `pip install -r requirements.txt`
* `createdb thecodebase`
* `python manage.py migrate`
* `python manage.py runserver`
