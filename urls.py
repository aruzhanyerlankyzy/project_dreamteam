from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login/registration/',views.registration, name='registration'),
    path('login/login_act/',views.login_act,name='sign_in'),
    path('login/registration/sign_up/', views.register, name="sign_up"),
    path('profile_premium/',views.profile_premium, name="profile_premium")
]