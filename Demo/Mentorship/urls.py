from django.urls import path
from Mentorship import views

urlpatterns = [
    path('',views.index, name='base'),
    path('registration/', views.registration, name='registration'),
]
