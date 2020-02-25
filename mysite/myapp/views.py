from django.http import HttpResponse
from django.shortcuts import render
import datetime

from myapp.models import Article


# // test function //
# def hello_world(request):
#     return HttpResponse('Hello World, IM!')

# def temp(request):
#     return render(request, 'temp.html', {
#         'value_datetime': datetime.date.today()
#         }
#     )

# def query_str(request):
#     return render(request, 'query.html', {
#         'test_user': request.GET['user'],
#         'test_message': request.GET['message']
#         }
#     )


# // CRUD //
def article_list(request):
    # return HttpResponse('投稿記事の一覧')
    articles = Article.objects.all().order_by('id')
    return render(request, 'article_list.html', {
        'articles': articles
        }
    )


def article_edit(request, article_id=None):
    return HttpResponse('投稿記事の編集')


def article_del(request, article_id):
    return HttpResponse('投稿記事の削除')
