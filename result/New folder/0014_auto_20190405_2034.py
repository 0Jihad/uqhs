# Generated by Django 2.1.3 on 2019-04-05 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0013_remove_qsubject_graded'),
    ]

    operations = [
        migrations.AddField(
            model_name='btutor',
            name='graded',
            field=models.ForeignKey(blank=True, help_text='Grade Counts', null=True, on_delete=django.db.models.deletion.CASCADE, to='result.RESULT_GRADE'),
        ),
        migrations.AlterField(
            model_name='result_grade',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='result.ASUBJECTS'),
        ),
    ]