# Generated by Django 2.1.3 on 2019-06-02 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0048_auto_20190526_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='btutor',
            name='session',
            field=models.CharField(blank=True, default='18/19', max_length=18, null=True),
        ),
    ]
