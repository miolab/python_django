from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world),
    path('temp/', views.temp),
    path('query/', views.query_str)
]
