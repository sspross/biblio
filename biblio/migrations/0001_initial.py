# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book'
        db.create_table('biblio_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
            ('opan', self.gf('django.db.models.fields.CharField')(max_length=14, blank=True)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=14, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('biblio', ['Book'])


    def backwards(self, orm):
        # Deleting model 'Book'
        db.delete_table('biblio_book')


    models = {
        'biblio.book': {
            'Meta': {'object_name': 'Book'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '14', 'blank': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'opan': ('django.db.models.fields.CharField', [], {'max_length': '14', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['biblio']