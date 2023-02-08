# FH Dortmund project

## Start development

1. Create virtual environment

`$ virtualenv -p python3.8 venv`

2. Create database (sqlite for local)

`$ python manage.py migrate`

3. Start project

`$ python manage.py runserver 127.0.0.1:8000`

4. Open browser http://127.0.0.1:8000