# Generated by Django 2.1.3 on 2019-04-08 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0016_auto_20190405_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='total',
            name='subject_by',
            field=models.ForeignKey(blank=True, help_text='subject_teacher', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
