# Generated by Django 2.1.3 on 2019-04-05 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0010_auto_20190401_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='RESULT_GRADE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_A', models.IntegerField(blank=True, null=True)),
                ('grade_C', models.IntegerField(blank=True, null=True)),
                ('grade_P', models.IntegerField(blank=True, null=True)),
                ('grade_F', models.IntegerField(blank=True, null=True)),
                ('grade_A1', models.IntegerField(blank=True, null=True)),
                ('grade_B2', models.IntegerField(blank=True, null=True)),
                ('grade_B3', models.IntegerField(blank=True, null=True)),
                ('grade_C4', models.IntegerField(blank=True, null=True)),
                ('grade_C5', models.IntegerField(blank=True, null=True)),
                ('grade_C6', models.IntegerField(blank=True, null=True)),
                ('grade_D7', models.IntegerField(blank=True, null=True)),
                ('grade_E8', models.IntegerField(blank=True, null=True)),
                ('grade_F9', models.IntegerField(blank=True, null=True)),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='result.BTUTOR')),
            ],
            options={
                'ordering': ('grade_A',),
            },
        ),
        migrations.AddField(
            model_name='qsubject',
            name='graded',
            field=models.ForeignKey(blank=True, help_text='Grade Counts', null=True, on_delete=django.db.models.deletion.CASCADE, to='result.RESULT_GRADE'),
        ),
    ]