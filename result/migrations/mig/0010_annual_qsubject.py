# Generated by Django 2.1.3 on 2019-06-21 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0009_auto_20190622_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='annual',
            name='qsubject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='result.QSUBJECT'),
        ),
    ]