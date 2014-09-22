# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WeekendPlan'
        db.create_table(u'weekend_weekendplan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('what_to_do', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('when', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('completed', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal(u'weekend', ['WeekendPlan'])


    def backwards(self, orm):
        # Deleting model 'WeekendPlan'
        db.delete_table(u'weekend_weekendplan')


    models = {
        u'weekend.weekendplan': {
            'Meta': {'object_name': 'WeekendPlan'},
            'completed': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'what_to_do': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'when': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['weekend']