# Generated by Django 2.1.3 on 2019-08-16 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0016_auto_20190814_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='btutor',
            name='created',
            field=models.DateTimeField(default='2019-08-17', max_length=200),
        ),
        migrations.AddField(
            model_name='btutor',
            name='updated',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
