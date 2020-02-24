from django.db import models


class Article(models.Model):
    title_submit = models.CharField(
        'Title',
        max_length=255
        )
    text_submit = models.TextField(
        'Text',
        blank=True,
        max_length=2000
        )

    def __str__(self):
        return self.title_submit
