
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="" ),
    
    path('register', views.Register, name="register"),

    path ('my-login', views.Login, name="my-login"),

    path('user-logout', views.Logout, name='user-logout'),
     
    #  CRUD

    path ('profile-dashboard', views.profile, name="profile-dashboard"),

    path('create-record', views.create_record, name='create-record'),

    path('update-record/<int:pk>', views.update_record, name='update-record'),

    path('record/<int:pk>', views.singular_record, name='record'),

    path('delete-record/<int:pk>', views.delete_record, name='delete-record'),
]