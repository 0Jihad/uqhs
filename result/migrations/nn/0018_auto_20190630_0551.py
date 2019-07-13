# Generated by Django 2.1.3 on 2019-06-29 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0017_auto_20190630_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='btutor',
            name='cader',
            field=models.CharField(blank=True, help_text='Senior/Junior', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='btutor',
            name='females',
            field=models.IntegerField(blank=True, default='0', help_text='Enter number of female in class', null=True),
        ),
        migrations.AlterField(
            model_name='btutor',
            name='males',
            field=models.IntegerField(blank=True, default='0', help_text='Enter number of male in class', null=True),
        ),
    ]