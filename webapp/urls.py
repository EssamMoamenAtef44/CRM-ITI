from django.urls import path
from .views import index, register, login, dashboard, logout, create_record, view_record
urlpatterns = [
   
    path('', index, name='index'),

    path('register/', register, name='register'),

    path('login/', login, name='login'),

    path('dashboard/', dashboard, name='dashboard'),

    path('logout/', logout, name='logout'),

    path('create_record/', create_record, name='create_record'),

    path('view_record/<int:record_id>/', view_record, name='view_record'),
    ]      