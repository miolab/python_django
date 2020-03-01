from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Article

import json
from collections import OrderedDict


# Create your views here.
def json_response(request, data, status=None):
    json_prepare = json.dumps(data, ensure_ascii=False, indent=2)
    callback = request.POST.get('callback')

    if not callback:
        callback = request.POST.get('callback')

    if callback:
        json_prepare = "%s(%s)" % (callback, json_prepare)
        response = HttpResponse(json_prepare, content_type='application/javascript; charset=UTF-8', status=status)
    else:
        response = HttpResponse(json_prepare, content_type='application/json; charset=UTF-8', status=status)

    return response


def article_list(request):
    articles = []

    for article in Article.objects.all().order_by('id'):
        article_dict = OrderedDict([
            ('id', article.id),
            ('Title', article.title_submit),
            ('Text', article.text_submit)
        ])
        articles.append(article_dict)

    data = OrderedDict([
        ('articles', articles)
    ])

    return json_response(request, data)
