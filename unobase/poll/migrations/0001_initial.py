# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PollQuestion'
        db.create_table(u'poll_pollquestion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('multiple_choice', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'poll', ['PollQuestion'])

        # Adding model 'PollAnswer'
        db.create_table(u'poll_pollanswer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers', to=orm['poll.PollQuestion'])),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('vote_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'poll', ['PollAnswer'])


    def backwards(self, orm):
        # Deleting model 'PollQuestion'
        db.delete_table(u'poll_pollquestion')

        # Deleting model 'PollAnswer'
        db.delete_table(u'poll_pollanswer')


    models = {
        u'poll.pollanswer': {
            'Meta': {'object_name': 'PollAnswer'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['poll.PollQuestion']"}),
            'vote_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'poll.pollquestion': {
            'Meta': {'object_name': 'PollQuestion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multiple_choice': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['poll']