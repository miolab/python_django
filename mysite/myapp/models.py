from django.db import models


class Article(models.Model):
    title_submit = models.CharField('Title', max_length=255)
    # date_submit = models.DateTimeField('Date')
    text_submit = models.TextField('Text', blank=True)

    def __str__(self):
        return self.title