from django.urls import path
from .views import *


urlpatterns = [
    path("",home,name='home'),
    path("confirm/<int:id>/",confirm,name='confirm'),
    path("bookings",bookings,name='bookings'),
    path('update/<int:id>/',update,name='update'),
    path('cancel/<int:id>/',cancel,name='cancel'),
    path('history',history,name='history'),
    path('register/',register,name='register'),
    path('login/',login_,name='login'),
    path('logout',logout_,name='logout'),
    path('profile/',profile,name='profile'),
    path('reset/',reset,name='reset'),
    path('pupdate/',pupdate,name='pupdate'),
    path('forgot_pasw/',forgot_pasw,name='forgot_pasw'),
    path('about/',about,name='about')
]
