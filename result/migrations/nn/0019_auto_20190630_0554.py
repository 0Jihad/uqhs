# Generated by Django 2.1.3 on 2019-06-29 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0018_auto_20190630_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='btutor',
            name='Class',
            field=models.CharField(blank=True, choices=[('JSS 1', 'jss_one'), ('JSS 2', 'jss_two'), ('JSS 3', 'jss_three'), ('SS 1', 'sss_one'), ('SS 2', 'sss_two'), ('SS 3', 'sss_three')], help_text='Select subject class', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='btutor',
            name='subject',
            field=models.ForeignKey(blank=True, help_text='Select subject', null=True, on_delete=django.db.models.deletion.SET_NULL, to='result.ASUBJECTS'),
        ),
        migrations.AlterField(
            model_name='btutor',
            name='term',
            field=models.CharField(blank=True, choices=[('1st Term', 'first term'), ('2nd Term', 'second term'), ('3rd Term', 'third term')], help_text='Select subject term', max_length=30, null=True),
        ),
    ]
