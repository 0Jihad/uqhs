# Generated by Django 2.1.3 on 2019-06-24 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('result', '0018_auto_20190624_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_subject',
            name='teacher_in',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='all_subject', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='btutor',
            name='teacher_in',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_account', to=settings.AUTH_USER_MODEL),
        ),
    ]
