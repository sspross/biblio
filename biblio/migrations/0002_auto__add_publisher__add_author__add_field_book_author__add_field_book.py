# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Publisher'
        db.create_table('biblio_publisher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('biblio', ['Publisher'])

        # Adding model 'Author'
        db.create_table('biblio_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('biblio', ['Author'])

        # Adding field 'Book.author'
        db.add_column('biblio_book', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='books', null=True, to=orm['biblio.Author']),
                      keep_default=False)

        # Adding field 'Book.publisher'
        db.add_column('biblio_book', 'publisher',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='books', null=True, to=orm['biblio.Publisher']),
                      keep_default=False)

        # Adding field 'Book.year'
        db.add_column('biblio_book', 'year',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Book.subtitle'
        db.add_column('biblio_book', 'subtitle',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Publisher'
        db.delete_table('biblio_publisher')

        # Deleting model 'Author'
        db.delete_table('biblio_author')

        # Deleting field 'Book.author'
        db.delete_column('biblio_book', 'author_id')

        # Deleting field 'Book.publisher'
        db.delete_column('biblio_book', 'publisher_id')

        # Deleting field 'Book.year'
        db.delete_column('biblio_book', 'year')

        # Deleting field 'Book.subtitle'
        db.delete_column('biblio_book', 'subtitle')


    models = {
        'biblio.author': {
            'Meta': {'object_name': 'Author'},
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'biblio.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'books'", 'null': 'True', 'to': "orm['biblio.Author']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '14', 'blank': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'opan': ('django.db.models.fields.CharField', [], {'max_length': '14', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'books'", 'null': 'True', 'to': "orm['biblio.Publisher']"}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'biblio.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['biblio']