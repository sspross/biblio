from django.db import models


class Book(models.Model):
    num = models.IntegerField('Nr.')
    opan = models.CharField('Opa Nr.', max_length=14, blank=True)
    isbn = models.CharField('ISBN', max_length=14, blank=True)
    title = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        if self.title:
            return self.title
        return self.isbn
