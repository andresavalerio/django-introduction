# Django introduction

The repository for the introductory Django project, created by the [Django community](https://www.djangoproject.com/start/), mainteined by Andresa Valério, built with :heart: and Python.

This source code has being the base to presentations on [@pinio](https://github.com/pinio) and Django girls.

## How to run

1. Clone this repository

2. Ensure that you have django installed in your machine
```
python -m django --version
```
You can also install it in a virtual environment
```
python -m venv .venv
source .venv/bin/activate
pip install django
```

3. Run the migrations with `python manage.py migrate`

4. To run tests, use `python manage.py test polls`

5. To run your project, use `python manage.py runserver` and go to http://localhost:8000/polls/

6. If you want to use the admin site, run `python manage.py createsuperuser`, choose a username, email and password for your admin profile and go to http://localhost:8000/admin/
