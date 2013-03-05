from django.db import models
from django.conf import settings


class Book(models.Model):
    num = models.IntegerField('Nr.')
    opan = models.CharField('Opa Nr.', max_length=14, blank=True)
    isbn = models.CharField('ISBN', max_length=14, blank=True)
    kind = models.IntegerField(choices=settings.OBJECT_KINDS, default=0)
    author = models.ForeignKey('biblio.Author', related_name='books', null=True, blank=True)
    publisher = models.ForeignKey('biblio.Publisher', related_name='books', null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=255, blank=True)
    subtitle = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Object'
        verbose_name_plural = 'Objects'

    def __unicode__(self):
        if self.title:
            return self.title
        return self.isbn


class Author(models.Model):
    lastname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        if self.firstname:
            return "%s, %s" % (self.lastname, self.firstname,)
        return self.lastname


class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
