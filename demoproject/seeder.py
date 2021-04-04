import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','demoproject.settings')

import django
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from studentapp.models import Student

#pip install faker
from faker import Faker
fg=Faker() 

def add_student():
    fname=fg.name() 
    femail=fg.email()
    fdob=fg.date()

    std=Student.objects.get_or_create(
        name=fname,
        email=femail,
        dob=fdob
    )  
    return std


def  populate_data(n=5):
    for x in range(n):
        std=add_student()

if __name__=='__main__':
    print('Populating Data Please Wait')
    print(':'*80)
    populate_data(10)
    print('Populating Data Complete')
    print(':'*80)

    try:
        user=User.objects.get_or_create(
            username='admin2',
            password=make_password('admin2'),
            email='admin1@gmail.com',
            first_name='super',
            last_name='user',
            is_staff=True,
            is_superuser=True,
            is_active=True,

        )

        user1=User.objects.get_or_create(
            username='ifte',
            password=make_password('ifte'),
            email='ifte@gmail.com',
            first_name='Iftekhar',
            last_name='Yousuf',
            is_staff=True,
            is_superuser=True,
            is_active=True,

        )
        print('super user creat successfully')
        print('#'*80)


        user2=User.objects.get_or_create(
            username='Sumon',
            password=make_password('@@@Error123'),
            email='sumonpol@gmail.com',
            first_name='Sumon',
            last_name='Pol',
            is_staff=True,
            is_superuser=False,
            is_active=True,

        )

        print('User creat successfully')
        print('#'*80)


    except:
        print('User already exists')

   