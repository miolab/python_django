from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import datetime

from myapp.models import Article
from myapp.forms import ArticleForm


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
    articles = Article.objects.all().order_by('id')
    return render(request, 'article_list.html', {
        'articles': articles
        }
    )


def article_edit(request, article_id=None):
    if article_id:
        article = get_object_or_404(Article, pk=article_id)
    else:
        article = Article()

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return redirect('myapp:article_list')
    else:
        form = ArticleForm(instance=article)

    return render(request, 'article_edit.html', dict(
        form=form,
        article_id=article_id
        )
    )


def article_del(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    return redirect('myapp:article_list')
