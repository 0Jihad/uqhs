# Generated by Django 2.1.3 on 2019-04-24 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0040_auto_20190425_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='qsubject',
            name='Class',
            field=models.CharField(blank=True, choices=[('JSS 1', 'jss_one'), ('JSS 2', 'jss_two'), ('JSS 3', 'jss_three'), ('SS 1', 'sss_one'), ('SS 2', 'sss_two'), ('SS 3', 'sss_three')], max_length=30, null=True),
        ),
    ]