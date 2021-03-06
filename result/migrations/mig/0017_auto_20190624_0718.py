# Generated by Django 2.1.3 on 2019-06-23 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0016_auto_20190624_0642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='first',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='second',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='third',
        ),
        migrations.RemoveField(
            model_name='all_subject',
            name='class_teacher',
        ),
        migrations.AlterField(
            model_name='btutor',
            name='user',
            field=models.ForeignKey(blank=True, help_text='loggon-account:move account here', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='btutor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='qsubject',
            name='logged_in',
            field=models.ForeignKey(blank=True, help_text='subject_teacher', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logins', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='TEACHER',
        ),
    ]
