# Generated by Django 2.1.3 on 2019-03-31 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_shelf', '0004_auto_20190401_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, default='None', null=True, verbose_name='died'),
        ),
    ]
