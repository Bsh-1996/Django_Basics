from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('detail/<int:todo_id>', views.detail, name= 'detail'),
    path('deete/<int:todo_id>', views.delete, name= 'delete'),
    path('create/', views.create, name= 'create'),
]



