from django.urls import path
from . import views


app_name = 'myapp'

urlpatterns = [
    # // test function //
    # path('hello/', views.hello_world),
    # path('temp/', views.temp),
    # path('query/', views.query_str),

    # // CRUD //
    path(
        'article/',
        views.article_list,
        name='article_list'
        ),
    path(
        'article/add/',
        views.article_edit,
        name='article_add'
        ),
    path(
        'article/modify/<int:article_id>',
        views.article_edit,
        name='article_modify'
        ),
    path(
        'article/del/<int:article_id>',
        views.article_del,
        name='article_del'
        ),
]
