# Generated by Django 2.1.3 on 2019-09-05 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0028_auto_20190903_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cname',
            name='Class',
        ),
        migrations.AddField(
            model_name='session',
            name='created',
            field=models.DateTimeField(default='2019-09-05', max_length=200),
        ),
        migrations.AddField(
            model_name='session',
            name='updated',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='btutor',
            name='created',
            field=models.DateTimeField(default='2019-09-05', max_length=200),
        ),
    ]
