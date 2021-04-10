from django.urls import path

from . import views

urlpatterns = [
    path('doctors_register',views.register,name='rgister'),
    path('doctors_logout',views.logout,name='logout'),
    path('doctors_login',views.login,name='login')

]