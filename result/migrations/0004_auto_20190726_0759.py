# Generated by Django 2.1.3 on 2019-07-25 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0003_auto_20190725_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit_user',
            name='account_id',
            field=models.CharField(blank=True, default=0, max_length=30, null=True),
        ),
    ]
