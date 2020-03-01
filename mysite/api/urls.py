from django.urls import path
from api import views


app_name = 'api'

urlpatterns = [
    # // test function //
    # path('hello/', views.hello_world),
    # path('temp/', views.temp),
    # path('query/', views.query_str),

    path('v1/articles', views.article_list, name='article_list')
]
