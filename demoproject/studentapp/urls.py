
from django.urls import path
from studentapp import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('details/<int:id>',views.details,name='details'),
    path('create/',views.create,name='create'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('send/',views.sendemail,name='send'),
]
