# Generated by Django 2.1.3 on 2019-08-10 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0014_auto_20190810_2211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annual',
            old_name='agr',
            new_name='Agr',
        ),
        migrations.RenameField(
            model_name='annual',
            old_name='anu_posi',
            new_name='Posi',
        ),
        migrations.RenameField(
            model_name='overall_annual',
            old_name='Agr',
            new_name='AGR',
        ),
        migrations.RenameField(
            model_name='overall_annual',
            old_name='Avr',
            new_name='AVR',
        ),
        migrations.RenameField(
            model_name='overall_annual',
            old_name='grade',
            new_name='GRD',
        ),
        migrations.RenameField(
            model_name='overall_annual',
            old_name='posi',
            new_name='POS',
        ),
        migrations.AlterField(
            model_name='overall_annual',
            name='acc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='acc', to='result.ANNUAL'),
        ),
        migrations.AlterField(
            model_name='overall_annual',
            name='agr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agr', to='result.ANNUAL'),
        ),
        migrations.AlterField(
            model_name='overall_annual',
            name='bst',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bst', to='result.ANNUAL'),
        ),
        migrations.AlterField(
            model_name='overall_annual',
            name='bus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bus', to='result.ANNUAL'),
        ),
        migrations.AlterField(
            model_name='overall_annual',
            name='eng',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='eng', to='result.ANNUAL'),
        ),
        migrations.AlterField(
            model_name='overall_annual',
            name='his',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='his', to='result.ANNUAL'),
        ),
        migrations.AlterField(
            model_name='overall_annual',
            name='ict',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='arb', to='result.ANNUAL'),
        ),
        migrations.AlterField(
            model_name='overall_annual',
            name='irs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='irs', to='result.ANNUAL'),
        ),
        migrations.AlterField(
            model_name='overall_annual',
            name='mat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mat', to='result.ANNUAL'),
        ),
        migrations.AlterField(
            model_name='overall_annual',
            name='nva',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nva', to='result.ANNUAL'),
        ),
        migrations.AlterField(
            model_name='overall_annual',
            name='prv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prv', to='result.ANNUAL'),
        ),
        migrations.AlterField(
            model_name='overall_annual',
            name='yor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='yor', to='result.ANNUAL'),
        ),
    ]