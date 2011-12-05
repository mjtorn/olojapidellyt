# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'UserProfile.about_me'
        db.add_column('web_userprofile', 'about_me', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'UserProfile.facebook_id'
        db.add_column('web_userprofile', 'facebook_id', self.gf('django.db.models.fields.BigIntegerField')(unique=True, null=True, blank=True), keep_default=False)

        # Adding field 'UserProfile.access_token'
        db.add_column('web_userprofile', 'access_token', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'UserProfile.facebook_name'
        db.add_column('web_userprofile', 'facebook_name', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'UserProfile.facebook_profile_url'
        db.add_column('web_userprofile', 'facebook_profile_url', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'UserProfile.website_url'
        db.add_column('web_userprofile', 'website_url', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'UserProfile.blog_url'
        db.add_column('web_userprofile', 'blog_url', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'UserProfile.image'
        db.add_column('web_userprofile', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'UserProfile.date_of_birth'
        db.add_column('web_userprofile', 'date_of_birth', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)

        # Adding field 'UserProfile.raw_data'
        db.add_column('web_userprofile', 'raw_data', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'UserProfile.about_me'
        db.delete_column('web_userprofile', 'about_me')

        # Deleting field 'UserProfile.facebook_id'
        db.delete_column('web_userprofile', 'facebook_id')

        # Deleting field 'UserProfile.access_token'
        db.delete_column('web_userprofile', 'access_token')

        # Deleting field 'UserProfile.facebook_name'
        db.delete_column('web_userprofile', 'facebook_name')

        # Deleting field 'UserProfile.facebook_profile_url'
        db.delete_column('web_userprofile', 'facebook_profile_url')

        # Deleting field 'UserProfile.website_url'
        db.delete_column('web_userprofile', 'website_url')

        # Deleting field 'UserProfile.blog_url'
        db.delete_column('web_userprofile', 'blog_url')

        # Deleting field 'UserProfile.image'
        db.delete_column('web_userprofile', 'image')

        # Deleting field 'UserProfile.date_of_birth'
        db.delete_column('web_userprofile', 'date_of_birth')

        # Deleting field 'UserProfile.raw_data'
        db.delete_column('web_userprofile', 'raw_data')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'web.story': {
            'Meta': {'object_name': 'Story'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mood': ('django.db.models.fields.IntegerField', [], {}),
            'posted_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['auth.User']", 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'})
        },
        'web.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'about_me': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'access_token': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'blog_url': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'facebook_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'facebook_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'facebook_profile_url': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'raw_data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'website_url': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['web']
