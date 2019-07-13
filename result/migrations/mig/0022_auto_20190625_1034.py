# Generated by Django 2.1.3 on 2019-06-24 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0021_auto_20190625_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='first',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='first', to='result.QSUBJECT'),
        ),
        migrations.AlterField(
            model_name='term',
            name='second',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second', to='result.QSUBJECT'),
        ),
        migrations.AlterField(
            model_name='term',
            name='third',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='third', to='result.QSUBJECT'),
        ),
    ]
