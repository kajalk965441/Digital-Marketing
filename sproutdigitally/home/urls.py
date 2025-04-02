from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.index, name="index"),
    path('about',views.company, name="company"),
    path('expertise',views.expertise, name="expertise"),
    path('contact',views.contact, name="contact")

]
