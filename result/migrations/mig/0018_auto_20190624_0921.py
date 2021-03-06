# Generated by Django 2.1.3 on 2019-06-23 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0017_auto_20190624_0718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='all_subject',
            old_name='arb',
            new_name='ict',
        ),
        migrations.AddField(
            model_name='all_subject',
            name='acc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='acc', to='result.TERM'),
        ),
        migrations.AlterField(
            model_name='asubjects',
            name='name',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Mathematics', 'Mathematics'), ('Civic Education', 'Civic Education'), ('Electrical', 'Electrical'), ('Yoruba', 'Yoruba'), ('Agric. Sc.', 'Agric. Sc.'), ('Garment Making', 'Garment Making'), ('Pre-Vocation', 'Pre-Vocation'), ('Information Technology', 'Information Technology'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('Geography', 'Geography'), ('Government', 'Government'), ('Account', 'Account'), ('Arabic', 'Arabic'), ('Islamic Studies', 'Islamic Studies'), ('Litrature', 'Litrature'), ('Commerce', 'Commerce'), ('Economics', 'Economics'), ('Business Studies', 'Business Studies'), ('Basic Science and Technology', 'Basic Science and Technology'), ('Catering', 'Catering'), ('National Value', 'National Value'), ('Furthe Mathematics', 'Furthe Mathematics'), ('History', 'History')], default='English', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='result_grade',
            name='subject',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Mathematics', 'Mathematics'), ('Civic Education', 'Civic Education'), ('Electrical', 'Electrical'), ('Yoruba', 'Yoruba'), ('Agric. Sc.', 'Agric. Sc.'), ('Garment Making', 'Garment Making'), ('Pre-Vocation', 'Pre-Vocation'), ('Information Technology', 'Information Technology'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('Geography', 'Geography'), ('Government', 'Government'), ('Account', 'Account'), ('Arabic', 'Arabic'), ('Islamic Studies', 'Islamic Studies'), ('Litrature', 'Litrature'), ('Commerce', 'Commerce'), ('Economics', 'Economics'), ('Business Studies', 'Business Studies'), ('Basic Science and Technology', 'Basic Science and Technology'), ('Catering', 'Catering'), ('National Value', 'National Value'), ('Furthe Mathematics', 'Furthe Mathematics'), ('History', 'History')], default='English', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='term',
            name='subject',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Mathematics', 'Mathematics'), ('Civic Education', 'Civic Education'), ('Electrical', 'Electrical'), ('Yoruba', 'Yoruba'), ('Agric. Sc.', 'Agric. Sc.'), ('Garment Making', 'Garment Making'), ('Pre-Vocation', 'Pre-Vocation'), ('Information Technology', 'Information Technology'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('Geography', 'Geography'), ('Government', 'Government'), ('Account', 'Account'), ('Arabic', 'Arabic'), ('Islamic Studies', 'Islamic Studies'), ('Litrature', 'Litrature'), ('Commerce', 'Commerce'), ('Economics', 'Economics'), ('Business Studies', 'Business Studies'), ('Basic Science and Technology', 'Basic Science and Technology'), ('Catering', 'Catering'), ('National Value', 'National Value'), ('Furthe Mathematics', 'Furthe Mathematics'), ('History', 'History')], default='English', max_length=30, null=True),
        ),
    ]
