# Generated by Django 2.1.3 on 2019-04-15 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0033_annual_model_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='btutor',
            name='model_in',
            field=models.CharField(blank=True, default='qsubject', max_length=8, null=True),
        ),
    ]