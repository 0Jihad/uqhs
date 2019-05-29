# Generated by Django 2.1.3 on 2019-03-11 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0004_auto_20190312_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit_user',
            name='bio',
            field=models.TextField(blank=True, help_text='am a native of ..................'),
        ),
        migrations.AlterField(
            model_name='edit_user',
            name='birth_date',
            field=models.DateField(blank=True, help_text='your birth date in this format: 01/20/1930.', null=True),
        ),
        migrations.AlterField(
            model_name='edit_user',
            name='city',
            field=models.CharField(blank=True, help_text='your main town', max_length=15),
        ),
        migrations.AlterField(
            model_name='edit_user',
            name='country',
            field=models.CharField(blank=True, help_text='your nationality.', max_length=10),
        ),
        migrations.AlterField(
            model_name='edit_user',
            name='department',
            field=models.CharField(blank=True, choices=[('Sc', 'Sciences'), ('SSc', 'Social Sciences'), ('Art', 'Arts and Humanities')], help_text="department you'r working", max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='edit_user',
            name='first_name',
            field=models.CharField(blank=True, help_text='your Nic Name may be included', max_length=20),
        ),
        migrations.AlterField(
            model_name='edit_user',
            name='last_name',
            field=models.CharField(blank=True, help_text='your Last Name', max_length=20),
        ),
        migrations.AlterField(
            model_name='edit_user',
            name='location',
            field=models.CharField(blank=True, help_text='where currently leaving', max_length=30),
        ),
        migrations.AlterField(
            model_name='edit_user',
            name='organization',
            field=models.CharField(blank=True, help_text='the group you belong', max_length=10),
        ),
        migrations.AlterField(
            model_name='edit_user',
            name='phone',
            field=models.CharField(blank=True, help_text='........ eg:08068302532.', max_length=20),
        ),
    ]
