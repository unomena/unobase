# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EULA'
        db.create_table(u'eula_eula', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
        ))
        db.send_create_signal(u'eula', ['EULA'])

        # Adding model 'EULAVersion'
        db.create_table(u'eula_eulaversion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('eula', self.gf('django.db.models.fields.related.ForeignKey')(related_name='instances', to=orm['eula.EULA'])),
            ('content', self.gf('ckeditor.fields.RichTextField')()),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date_created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'eula', ['EULAVersion'])


    def backwards(self, orm):
        # Deleting model 'EULA'
        db.delete_table(u'eula_eula')

        # Deleting model 'EULAVersion'
        db.delete_table(u'eula_eulaversion')


    models = {
        u'eula.eula': {
            'Meta': {'object_name': 'EULA'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'eula.eulaversion': {
            'Meta': {'ordering': "['-date_created']", 'object_name': 'EULAVersion'},
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'eula': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'to': u"orm['eula.EULA']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['eula']