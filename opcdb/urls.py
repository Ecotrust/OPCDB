from django.urls import path
from . import views

app_name = 'opcdb'
urlpatterns = [
    path('', views.home_page, name='home'),
]
