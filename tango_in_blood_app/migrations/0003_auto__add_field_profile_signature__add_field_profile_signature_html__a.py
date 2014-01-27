# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Profile.signature'
        db.add_column(u'tango_in_blood_app_profile', 'signature',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=1024, blank=True),
                      keep_default=False)

        # Adding field 'Profile.signature_html'
        db.add_column(u'tango_in_blood_app_profile', 'signature_html',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=1054, blank=True),
                      keep_default=False)

        # Adding field 'Profile.time_zone'
        db.add_column(u'tango_in_blood_app_profile', 'time_zone',
                      self.gf('django.db.models.fields.FloatField')(default=3.0),
                      keep_default=False)

        # Adding field 'Profile.language'
        db.add_column(u'tango_in_blood_app_profile', 'language',
                      self.gf('django.db.models.fields.CharField')(default='en-us', max_length=10, blank=True),
                      keep_default=False)

        # Adding field 'Profile.show_signatures'
        db.add_column(u'tango_in_blood_app_profile', 'show_signatures',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Profile.post_count'
        db.add_column(u'tango_in_blood_app_profile', 'post_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Profile.autosubscribe'
        db.add_column(u'tango_in_blood_app_profile', 'autosubscribe',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


        # Changing field 'Profile.avatar'
        db.alter_column(u'tango_in_blood_app_profile', 'avatar', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True))

    def backwards(self, orm):
        # Deleting field 'Profile.signature'
        db.delete_column(u'tango_in_blood_app_profile', 'signature')

        # Deleting field 'Profile.signature_html'
        db.delete_column(u'tango_in_blood_app_profile', 'signature_html')

        # Deleting field 'Profile.time_zone'
        db.delete_column(u'tango_in_blood_app_profile', 'time_zone')

        # Deleting field 'Profile.language'
        db.delete_column(u'tango_in_blood_app_profile', 'language')

        # Deleting field 'Profile.show_signatures'
        db.delete_column(u'tango_in_blood_app_profile', 'show_signatures')

        # Deleting field 'Profile.post_count'
        db.delete_column(u'tango_in_blood_app_profile', 'post_count')

        # Deleting field 'Profile.autosubscribe'
        db.delete_column(u'tango_in_blood_app_profile', 'autosubscribe')


        # Changing field 'Profile.avatar'
        db.alter_column(u'tango_in_blood_app_profile', 'avatar', self.gf('django.db.models.fields.URLField')(default='', max_length=200))

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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tango_in_blood_app.profile': {
            'Meta': {'object_name': 'Profile'},
            'autosubscribe': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'avatar': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '6000', 'blank': 'True'}),
            'conversion_password': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40', 'blank': 'True'}),
            'converted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'profile_converted_bys'", 'null': 'True', 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en-us'", 'max_length': '10', 'blank': 'True'}),
            'post_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'show_signatures': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'signature': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'blank': 'True'}),
            'signature_html': ('django.db.models.fields.TextField', [], {'max_length': '1054', 'blank': 'True'}),
            'time_zone': ('django.db.models.fields.FloatField', [], {'default': '3.0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profile_users'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['tango_in_blood_app']