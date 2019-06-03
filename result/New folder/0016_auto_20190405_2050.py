# Generated by Django 2.1.3 on 2019-04-05 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0015_result_grade_remark'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='result_grade',
            options={'ordering': ('subject',)},
        ),
        migrations.AlterField(
            model_name='result_grade',
            name='subject',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Mathematics', 'Mathematics'), ('Civic Education', 'Civic Education'), ('Electrical', 'Electrical'), ('Yoruba', 'Yoruba'), ('Agric. Sc.', 'Agric. Sc.'), ('Garment Making', 'Garment Making'), ('Pre-Vocation', 'Pre-Vocation'), ('Information Technology', 'Information Technology'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('Geography', 'Geography'), ('Government', 'Government'), ('Account', 'Account'), ('Arabic', 'Arabic'), ('Islamic Studies', 'Islamic Studies'), ('Litrature', 'Litrature'), ('Commerce', 'Commerce'), ('Economics', 'Economics'), ('Business Studies', 'Business Studies'), ('Basic Science and Technology', 'Basic Science and Technology'), ('Catering', 'Catering'), ('National Value', 'National Value'), ('Furthe Mathematics', 'Furthe Mathematics'), ('others', 'others')], default='English', max_length=30, null=True),
        ),
    ]