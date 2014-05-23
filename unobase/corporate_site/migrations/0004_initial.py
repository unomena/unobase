# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'corporate_site_article', (
            (u'relatedmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['unobase.RelatedModel'], unique=True)),
            (u'auditmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['unobase.AuditModel'], unique=True)),
            (u'tagmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['unobase.TagModel'], unique=True, primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('date_taken', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('view_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('crop_from', self.gf('django.db.models.fields.CharField')(default='center', max_length=10, blank=True)),
            ('effect', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='article_related', null=True, to=orm['photologue.PhotoEffect'])),
            ('state', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('publish_date_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('retract_date_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('content', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
            ('image_name', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'corporate_site', ['Article'])

        # Adding M2M table for field sites on 'Article'
        m2m_table_name = db.shorten_name(u'corporate_site_article_sites')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm[u'corporate_site.article'], null=False)),
            ('site', models.ForeignKey(orm[u'sites.site'], null=False))
        ))
        db.create_unique(m2m_table_name, ['article_id', 'site_id'])

        # Adding model 'News'
        db.create_table(u'corporate_site_news', (
            (u'article_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['corporate_site.Article'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'corporate_site', ['News'])

        # Adding model 'Award'
        db.create_table(u'corporate_site_award', (
            (u'article_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['corporate_site.Article'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'corporate_site', ['Award'])

        # Adding model 'PressRelease'
        db.create_table(u'corporate_site_pressrelease', (
            (u'article_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['corporate_site.Article'], unique=True, primary_key=True)),
            ('pdf', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('external_link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'corporate_site', ['PressRelease'])

        # Adding model 'MediaCoverage'
        db.create_table(u'corporate_site_mediacoverage', (
            (u'article_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['corporate_site.Article'], unique=True, primary_key=True)),
            ('pdf', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('external_link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'corporate_site', ['MediaCoverage'])

        # Adding model 'Event'
        db.create_table(u'corporate_site_event', (
            (u'relatedmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['unobase.RelatedModel'], unique=True)),
            (u'event_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['calendar.Event'], unique=True, primary_key=True)),
            ('state', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('publish_date_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('retract_date_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('image_name', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'corporate_site', ['Event'])

        # Adding model 'Vacancy'
        db.create_table(u'corporate_site_vacancy', (
            (u'auditmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['unobase.AuditModel'], unique=True)),
            (u'tagmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['unobase.TagModel'], unique=True, primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('date_taken', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('view_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('crop_from', self.gf('django.db.models.fields.CharField')(default='center', max_length=10, blank=True)),
            ('effect', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='vacancy_related', null=True, to=orm['photologue.PhotoEffect'])),
            ('state', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('publish_date_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('retract_date_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('content', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
            ('external_link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'corporate_site', ['Vacancy'])

        # Adding M2M table for field sites on 'Vacancy'
        m2m_table_name = db.shorten_name(u'corporate_site_vacancy_sites')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('vacancy', models.ForeignKey(orm[u'corporate_site.vacancy'], null=False)),
            ('site', models.ForeignKey(orm[u'sites.site'], null=False))
        ))
        db.create_unique(m2m_table_name, ['vacancy_id', 'site_id'])

        # Adding model 'Product'
        db.create_table(u'corporate_site_product', (
            (u'relatedmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['unobase.RelatedModel'], unique=True)),
            (u'auditmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['unobase.AuditModel'], unique=True)),
            (u'tagmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['unobase.TagModel'], unique=True, primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('date_taken', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('view_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('crop_from', self.gf('django.db.models.fields.CharField')(default='center', max_length=10, blank=True)),
            ('effect', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='product_related', null=True, to=orm['photologue.PhotoEffect'])),
            ('state', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('publish_date_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('retract_date_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('content', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('image_name', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'corporate_site', ['Product'])

        # Adding M2M table for field sites on 'Product'
        m2m_table_name = db.shorten_name(u'corporate_site_product_sites')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'corporate_site.product'], null=False)),
            ('site', models.ForeignKey(orm[u'sites.site'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'site_id'])

        # Adding model 'CompanyMember'
        db.create_table(u'corporate_site_companymember', (
            (u'auditmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['unobase.AuditModel'], unique=True)),
            (u'tagmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['unobase.TagModel'], unique=True, primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('date_taken', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('view_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('crop_from', self.gf('django.db.models.fields.CharField')(default='center', max_length=10, blank=True)),
            ('effect', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='companymember_related', null=True, to=orm['photologue.PhotoEffect'])),
            ('state', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('publish_date_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('retract_date_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('content', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
            ('is_board_member', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_leader', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_investor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('job_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('image_name', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True, blank=True)),
            ('twitter_handle', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('linked_in_handle', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('facebook_handle', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'corporate_site', ['CompanyMember'])

        # Adding M2M table for field sites on 'CompanyMember'
        m2m_table_name = db.shorten_name(u'corporate_site_companymember_sites')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('companymember', models.ForeignKey(orm[u'corporate_site.companymember'], null=False)),
            ('site', models.ForeignKey(orm[u'sites.site'], null=False))
        ))
        db.create_unique(m2m_table_name, ['companymember_id', 'site_id'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'corporate_site_article')

        # Removing M2M table for field sites on 'Article'
        db.delete_table(db.shorten_name(u'corporate_site_article_sites'))

        # Deleting model 'News'
        db.delete_table(u'corporate_site_news')

        # Deleting model 'Award'
        db.delete_table(u'corporate_site_award')

        # Deleting model 'PressRelease'
        db.delete_table(u'corporate_site_pressrelease')

        # Deleting model 'MediaCoverage'
        db.delete_table(u'corporate_site_mediacoverage')

        # Deleting model 'Event'
        db.delete_table(u'corporate_site_event')

        # Deleting model 'Vacancy'
        db.delete_table(u'corporate_site_vacancy')

        # Removing M2M table for field sites on 'Vacancy'
        db.delete_table(db.shorten_name(u'corporate_site_vacancy_sites'))

        # Deleting model 'Product'
        db.delete_table(u'corporate_site_product')

        # Removing M2M table for field sites on 'Product'
        db.delete_table(db.shorten_name(u'corporate_site_product_sites'))

        # Deleting model 'CompanyMember'
        db.delete_table(u'corporate_site_companymember')

        # Removing M2M table for field sites on 'CompanyMember'
        db.delete_table(db.shorten_name(u'corporate_site_companymember_sites'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'calendar.event': {
            'Meta': {'ordering': "('start',)", 'object_name': 'Event'},
            u'auditmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['unobase.AuditModel']", 'unique': 'True'}),
            'content': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'event_related'", 'null': 'True', 'to': u"orm['photologue.PhotoEffect']"}),
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'external_link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'repeat': ('django.db.models.fields.CharField', [], {'default': "'does_not_repeat'", 'max_length': '64'}),
            'repeat_until': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            u'tagmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['unobase.TagModel']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calendar.Venue']", 'null': 'True', 'blank': 'True'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'calendar.venue': {
            'Meta': {'object_name': 'Venue'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'corporate_site.article': {
            'Meta': {'object_name': 'Article', '_ormbases': [u'unobase.RelatedModel']},
            u'auditmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['unobase.AuditModel']", 'unique': 'True'}),
            'content': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'article_related'", 'null': 'True', 'to': u"orm['photologue.PhotoEffect']"}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'image_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'publish_date_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'relatedmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['unobase.RelatedModel']", 'unique': 'True'}),
            'retract_date_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'tagmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['unobase.TagModel']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'corporate_site.award': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Award', '_ormbases': [u'corporate_site.Article']},
            u'article_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['corporate_site.Article']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'corporate_site.companymember': {
            'Meta': {'ordering': "['order']", 'object_name': 'CompanyMember'},
            u'auditmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['unobase.AuditModel']", 'unique': 'True'}),
            'content': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'companymember_related'", 'null': 'True', 'to': u"orm['photologue.PhotoEffect']"}),
            'facebook_handle': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'image_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'is_board_member': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_investor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_leader': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'linked_in_handle': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'publish_date_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'retract_date_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'tagmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['unobase.TagModel']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'twitter_handle': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'corporate_site.event': {
            'Meta': {'ordering': "['-start']", 'object_name': 'Event', '_ormbases': [u'calendar.Event', u'unobase.RelatedModel']},
            u'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['calendar.Event']", 'unique': 'True', 'primary_key': 'True'}),
            'image_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'publish_date_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'relatedmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['unobase.RelatedModel']", 'unique': 'True'}),
            'retract_date_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'corporate_site.mediacoverage': {
            'Meta': {'ordering': "['-publish_date_time']", 'object_name': 'MediaCoverage', '_ormbases': [u'corporate_site.Article']},
            u'article_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['corporate_site.Article']", 'unique': 'True', 'primary_key': 'True'}),
            'external_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'corporate_site.news': {
            'Meta': {'ordering': "['-publish_date_time']", 'object_name': 'News', '_ormbases': [u'corporate_site.Article']},
            u'article_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['corporate_site.Article']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'corporate_site.pressrelease': {
            'Meta': {'ordering': "['-publish_date_time']", 'object_name': 'PressRelease', '_ormbases': [u'corporate_site.Article']},
            u'article_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['corporate_site.Article']", 'unique': 'True', 'primary_key': 'True'}),
            'external_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'corporate_site.product': {
            'Meta': {'object_name': 'Product', '_ormbases': [u'unobase.RelatedModel']},
            u'auditmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['unobase.AuditModel']", 'unique': 'True'}),
            'content': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'product_related'", 'null': 'True', 'to': u"orm['photologue.PhotoEffect']"}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'image_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'publish_date_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'relatedmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['unobase.RelatedModel']", 'unique': 'True'}),
            'retract_date_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'tagmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['unobase.TagModel']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'corporate_site.vacancy': {
            'Meta': {'object_name': 'Vacancy'},
            u'auditmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['unobase.AuditModel']", 'unique': 'True'}),
            'content': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'vacancy_related'", 'null': 'True', 'to': u"orm['photologue.PhotoEffect']"}),
            'external_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'publish_date_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'retract_date_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'tagmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['unobase.TagModel']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'downloads.download': {
            'Meta': {'object_name': 'Download'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'downloads.downloadversion': {
            'Meta': {'ordering': "['-date_created']", 'object_name': 'DownloadVersion'},
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'download': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'to': u"orm['downloads.Download']"}),
            'eula_required': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'download_versions'", 'null': 'True', 'to': u"orm['eula.EULAVersion']"}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_downloadable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
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
        },
        u'photologue.photoeffect': {
            'Meta': {'object_name': 'PhotoEffect'},
            'background_color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFFF'", 'max_length': '7'}),
            'brightness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'color': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'contrast': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'filters': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'reflection_size': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reflection_strength': ('django.db.models.fields.FloatField', [], {'default': '0.6'}),
            'sharpness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'transpose_method': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'tagging.tag': {
            'Meta': {'ordering': "['-publish_date_time']", 'object_name': 'Tag'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publish_date_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'retract_date_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'unobase.auditmodel': {
            'Meta': {'object_name': 'AuditModel'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_objects'", 'null': 'True', 'to': u"orm['user.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leaf_content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'modified_objects'", 'null': 'True', 'to': u"orm['user.User']"})
        },
        u'unobase.relatedmodel': {
            'Meta': {'object_name': 'RelatedModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'related': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['unobase.RelatedModel']", 'null': 'True', 'blank': 'True'}),
            'related_leaf_content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True'})
        },
        u'unobase.tagmodel': {
            'Meta': {'object_name': 'TagModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leaf_content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'tag_models'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['tagging.Tag']"})
        },
        u'user.user': {
            'Meta': {'object_name': 'User'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'd_and_b': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'user_related'", 'null': 'True', 'to': u"orm['photologue.PhotoEffect']"}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'eulas_accepted': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'users_accepted'", 'to': u"orm['eula.EULAVersion']", 'through': u"orm['user.UserEULA']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'files_downloaded': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'users_downloaded'", 'to': u"orm['downloads.DownloadVersion']", 'through': u"orm['user.UserDownload']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_console_user': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'legal_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'login_token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'login_token_init_vector': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'maturation_score': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'newsletter_recipient': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.PositiveIntegerField', [], {'default': '100'}),
            'salesforce_account_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'salesforce_contact_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'salesforce_lead_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'salesforce_subscription_level': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'state_province': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'street_address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tax_id_vat_gst_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'web_address': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'zip_postal_code': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'})
        },
        u'user.userdownload': {
            'Meta': {'object_name': 'UserDownload'},
            'download_version': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['downloads.DownloadVersion']"}),
            'downloaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['user.User']"})
        },
        u'user.usereula': {
            'Meta': {'object_name': 'UserEULA'},
            'eula': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eula.EULAVersion']"}),
            'eula_content': ('ckeditor.fields.RichTextField', [], {}),
            'file_signed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['downloads.DownloadVersion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'signed_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['user.User']"})
        }
    }

    complete_apps = ['corporate_site']