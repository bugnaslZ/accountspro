from django.urls import path
from .views import *
app_name = 'accounts'

urlpatterns = [
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('signup/',signup_user,name='signup'),
    path('reset_pasword/',reset_pasword,name='reset_pasword'),
    path('reset_pasword_done/',reset_pasword_done,name='reset_pasword_done'),
    path('reset_pasword_coniform/',reset_pasword_coniform,name='reset_pasword_coniform'),
    path('reset_pasword_complate/',reset_pasword_complate,name='reset_pasword_complate'),
    path('edit_profile/',edit_profile,name='edit_profile')
]