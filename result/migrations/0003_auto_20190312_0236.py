# Generated by Django 2.1.3 on 2019-03-11 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0002_auto_20190312_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit_user',
            name='city',
            field=models.CharField(blank=True, help_text='Ibadan.', max_length=15),
        ),
        migrations.AlterField(
            model_name='edit_user',
            name='country',
            field=models.CharField(blank=True, help_text='Nigeria.', max_length=10),
        ),
        migrations.AlterField(
            model_name='edit_user',
            name='last_name',
            field=models.CharField(blank=True, help_text='Your Nic Name inclussive', max_length=20),
        ),
        migrations.AlterField(
            model_name='edit_user',
            name='organization',
            field=models.CharField(blank=True, help_text='IIRO.', max_length=10),
        ),
    ]
