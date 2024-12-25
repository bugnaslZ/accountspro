from django.urls import path
from .views import home,agent,about,contact
app_name = 'home'
urlpatterns = [
    path('',home,name='home'),
    path('agent',agent,name='agent'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
]