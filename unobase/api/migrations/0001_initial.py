# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Destination'
        db.create_table(u'api_destination', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Destination'])

        # Adding model 'Service'
        db.create_table(u'api_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('destination', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Destination'])),
            ('retries', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=3)),
            ('success_string', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('error_string', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Service'])

        # Adding model 'Request'
        db.create_table(u'api_request', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Service'])),
            ('request_data', self.gf('django.db.models.fields.TextField')()),
            ('response_data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('created_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('completed_timestamp', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Request'])

        # Adding model 'RequestLog'
        db.create_table(u'api_requestlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('request', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Request'])),
            ('action', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('result', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('narration', self.gf('django.db.models.fields.TextField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['RequestLog'])


    def backwards(self, orm):
        # Deleting model 'Destination'
        db.delete_table(u'api_destination')

        # Deleting model 'Service'
        db.delete_table(u'api_service')

        # Deleting model 'Request'
        db.delete_table(u'api_request')

        # Deleting model 'RequestLog'
        db.delete_table(u'api_requestlog')


    models = {
        u'api.destination': {
            'Meta': {'object_name': 'Destination'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'api.request': {
            'Meta': {'object_name': 'Request'},
            'completed_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request_data': ('django.db.models.fields.TextField', [], {}),
            'response_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Service']"}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'api.requestlog': {
            'Meta': {'object_name': 'RequestLog'},
            'action': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'narration': ('django.db.models.fields.TextField', [], {}),
            'request': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Request']"}),
            'result': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'api.service': {
            'Meta': {'object_name': 'Service'},
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Destination']"}),
            'error_string': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'retries': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '3'}),
            'success_string': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['api']