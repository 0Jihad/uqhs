# Generated by Django 2.1.3 on 2019-04-24 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0039_auto_20190425_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qsubject',
            name='tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='result.BTUTOR'),
        ),
    ]