''' Contact app URLs '''
from django.urls import path
from contact import views

app_name: str = 'contact'

urlpatterns: list = [
    path('', views.index, name='index'),
]
