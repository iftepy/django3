day8
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
creat student model.
after creating model we have to migrate.
=> python manage.py makemigrations
=> python manage.py migrate

from django.contrib import admin
from studentapp.models import Student
# Register your models here.

admin.site.register(Student)
now Create superuser 
=>python manage.py createsuperuser

user Name=admin
password=123

pip install django-crispy-forms