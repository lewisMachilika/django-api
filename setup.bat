call python -m venv C:\pythonenvs\cyb-client-env
call python -m C:\pythonenvs\cyb-client-env\Scripts\activate
call python -m pip install -r .\requirements.txt
call python manage.py makemigrations
call python manage.py migrate
call python manage.py createsuperuser

