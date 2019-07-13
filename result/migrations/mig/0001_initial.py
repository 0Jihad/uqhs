# Generated by Django 2.1.3 on 2019-06-02 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import result.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ANNUAL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.FloatField(blank=True, max_length=4, null=True)),
                ('second', models.FloatField(blank=True, max_length=4, null=True)),
                ('third', models.FloatField(blank=True, max_length=4, null=True)),
                ('anual', models.FloatField(blank=True, max_length=10, null=True)),
                ('agr', models.FloatField(blank=True, max_length=10, null=True)),
                ('grade', models.CharField(blank=True, max_length=5, null=True)),
                ('anu_posi', models.CharField(blank=True, max_length=5, null=True)),
                ('term', models.CharField(blank=True, default='None', max_length=15, null=True)),
                ('model_in', models.CharField(blank=True, default='None', max_length=15, null=True)),
                ('logged_in', models.ForeignKey(blank=True, help_text='subject_teacher', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('student_name_id',),
            },
        ),
        migrations.CreateModel(
            name='ASUBJECTS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('English', 'English'), ('Mathematics', 'Mathematics'), ('Civic Education', 'Civic Education'), ('Electrical', 'Electrical'), ('Yoruba', 'Yoruba'), ('Agric. Sc.', 'Agric. Sc.'), ('Garment Making', 'Garment Making'), ('Pre-Vocation', 'Pre-Vocation'), ('Information Technology', 'Information Technology'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('Geography', 'Geography'), ('Government', 'Government'), ('Account', 'Account'), ('Arabic', 'Arabic'), ('Islamic Studies', 'Islamic Studies'), ('Litrature', 'Litrature'), ('Commerce', 'Commerce'), ('Economics', 'Economics'), ('Business Studies', 'Business Studies'), ('Basic Science and Technology', 'Basic Science and Technology'), ('Catering', 'Catering'), ('National Value', 'National Value'), ('Furthe Mathematics', 'Furthe Mathematics'), ('others', 'others')], default='English', max_length=30, null=True)),
                ('model_in', models.CharField(blank=True, default='subject', max_length=8, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='BTUTOR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(blank=True, max_length=30, null=True)),
                ('Class', models.CharField(blank=True, choices=[('JSS 1', 'jss_one'), ('JSS 2', 'jss_two'), ('JSS 3', 'jss_three'), ('SS 1', 'sss_one'), ('SS 2', 'sss_two'), ('SS 3', 'sss_three')], max_length=30, null=True)),
                ('term', models.CharField(blank=True, choices=[('1st Term', 'first term'), ('2nd Term', 'second term'), ('3rd Term', 'third term')], max_length=30, null=True)),
                ('model_summary', models.CharField(blank=True, default='tutor', max_length=1000, null=True)),
                ('model_in', models.CharField(blank=True, default='qsubject', max_length=8, null=True)),
                ('males', models.IntegerField(blank=True, default='0', null=True)),
                ('females', models.IntegerField(blank=True, default='0', null=True)),
                ('cader', models.CharField(blank=True, max_length=1, null=True)),
                ('session', models.IntegerField(blank=True, default='0', null=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='CNAME',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(blank=True, max_length=30, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(blank=True, editable=False, null=True)),
                ('subject_code', models.IntegerField(blank=True, default='0', null=True)),
                ('model_summary', models.CharField(blank=True, default='student_names', max_length=200, null=True)),
                ('Class', models.CharField(blank=True, default='None', max_length=200, null=True)),
            ],
            options={
                'ordering': ('student_name',),
            },
        ),
        migrations.CreateModel(
            name='Edit_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=20)),
                ('first_name', models.CharField(blank=True, max_length=20)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='static/result/', validators=[result.models.Edit_User.validate_image])),
                ('bio', models.TextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=15)),
                ('country', models.CharField(blank=True, max_length=10)),
                ('organization', models.CharField(blank=True, max_length=10)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, help_text='Date format: MM/DD/YYYY', null=True)),
                ('department', models.CharField(blank=True, choices=[('Sc', 'Sciences'), ('SSc', 'Social Sciences'), ('Art', 'Arts and Humanities')], max_length=30, null=True)),
                ('account', models.CharField(blank=True, choices=[('Student', 'Student'), ('Staff', 'Staff')], max_length=30, null=True)),
                ('email_confirmed', models.BooleanField(default=False, help_text='True/False')),
                ('model_in', models.CharField(blank=True, default='user_profile', max_length=15, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('account',),
            },
        ),
        migrations.CreateModel(
            name='QSUBJECT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.FloatField(blank=True, max_length=4, null=True)),
                ('agn', models.FloatField(blank=True, max_length=4, null=True)),
                ('atd', models.FloatField(blank=True, max_length=4, null=True)),
                ('total', models.FloatField(blank=True, max_length=4, null=True)),
                ('exam', models.FloatField(blank=True, max_length=4, null=True)),
                ('agr', models.FloatField(blank=True, max_length=4, null=True)),
                ('grade', models.CharField(blank=True, max_length=5, null=True)),
                ('posi', models.CharField(blank=True, max_length=5, null=True)),
                ('gender', models.CharField(blank=True, help_text='sex', max_length=10, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(blank=True, editable=False, null=True)),
                ('cader', models.CharField(blank=True, choices=[('s', 'Senior'), ('j', 'Junior')], max_length=1, null=True)),
                ('model_in', models.CharField(blank=True, default='qsubject', max_length=8, null=True)),
                ('annual_scores', models.CharField(blank=True, max_length=100, null=True)),
                ('Class', models.CharField(blank=True, choices=[('JSS 1', 'jss_one'), ('JSS 2', 'jss_two'), ('JSS 3', 'jss_three'), ('SS 1', 'sss_one'), ('SS 2', 'sss_two'), ('SS 3', 'sss_three')], max_length=30, null=True)),
                ('logged_in', models.ForeignKey(blank=True, help_text='subject_teacher', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('student_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='result.CNAME')),
                ('tutor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='result.BTUTOR')),
            ],
            options={
                'ordering': ('student_name_id',),
            },
        ),
        migrations.CreateModel(
            name='QUEST_MODEL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.FloatField(blank=True, max_length=4, null=True)),
                ('agn', models.FloatField(blank=True, max_length=4, null=True)),
                ('atd', models.FloatField(blank=True, max_length=4, null=True)),
                ('total', models.FloatField(blank=True, max_length=4, null=True)),
                ('exam', models.FloatField(blank=True, max_length=4, null=True)),
                ('agr', models.FloatField(blank=True, max_length=4, null=True)),
                ('grade', models.CharField(blank=True, max_length=5, null=True)),
                ('posi', models.CharField(blank=True, max_length=5, null=True)),
                ('gender', models.CharField(blank=True, help_text='sex', max_length=10, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(blank=True, editable=False, null=True)),
                ('cader', models.CharField(blank=True, max_length=1, null=True)),
                ('model_in', models.CharField(blank=True, default='qsubject', max_length=8, null=True)),
                ('logged_in', models.ForeignKey(blank=True, help_text='subject_teacher', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('student_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='result.CNAME')),
                ('tutor', models.ForeignKey(blank=True, help_text='terms', null=True, on_delete=django.db.models.deletion.CASCADE, to='result.BTUTOR')),
            ],
        ),
        migrations.CreateModel(
            name='RESULT_GRADE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.IntegerField(blank=True, default='0', null=True)),
                ('model_in', models.CharField(blank=True, default='grades', max_length=6, null=True)),
                ('subject', models.CharField(blank=True, choices=[('English', 'English'), ('Mathematics', 'Mathematics'), ('Civic Education', 'Civic Education'), ('Electrical', 'Electrical'), ('Yoruba', 'Yoruba'), ('Agric. Sc.', 'Agric. Sc.'), ('Garment Making', 'Garment Making'), ('Pre-Vocation', 'Pre-Vocation'), ('Information Technology', 'Information Technology'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('Geography', 'Geography'), ('Government', 'Government'), ('Account', 'Account'), ('Arabic', 'Arabic'), ('Islamic Studies', 'Islamic Studies'), ('Litrature', 'Litrature'), ('Commerce', 'Commerce'), ('Economics', 'Economics'), ('Business Studies', 'Business Studies'), ('Basic Science and Technology', 'Basic Science and Technology'), ('Catering', 'Catering'), ('National Value', 'National Value'), ('Furthe Mathematics', 'Furthe Mathematics'), ('others', 'others')], default='English', max_length=30, null=True)),
                ('grade_A', models.IntegerField(blank=True, default='0', null=True)),
                ('grade_C', models.IntegerField(blank=True, default='0', null=True)),
                ('grade_P', models.IntegerField(blank=True, default='0', null=True)),
                ('grade_F', models.IntegerField(blank=True, default='0', null=True)),
                ('grade_A1', models.IntegerField(blank=True, default='0', null=True)),
                ('grade_B2', models.IntegerField(blank=True, default='0', null=True)),
                ('grade_B3', models.IntegerField(blank=True, default='0', null=True)),
                ('grade_C4', models.IntegerField(blank=True, default='0', null=True)),
                ('grade_C5', models.IntegerField(blank=True, default='0', null=True)),
                ('grade_C6', models.IntegerField(blank=True, default='0', null=True)),
                ('grade_D7', models.IntegerField(blank=True, default='0', null=True)),
                ('grade_E8', models.IntegerField(blank=True, default='0', null=True)),
                ('grade_F9', models.IntegerField(blank=True, default='0', null=True)),
                ('remark', models.BooleanField(default=False, help_text='True/False')),
            ],
            options={
                'ordering': ('subject',),
            },
        ),
        migrations.CreateModel(
            name='TOTAL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_scores', models.FloatField(blank=True, max_length=9, null=True)),
                ('subject_pert', models.FloatField(blank=True, max_length=9, null=True)),
                ('term', models.CharField(blank=True, choices=[('1st Term', 'first term'), ('2nd Term', 'second term'), ('3rd Term', 'third term')], help_text='subject term', max_length=30, null=True)),
                ('model_in', models.CharField(blank=True, default='total', max_length=6, null=True)),
                ('logged_in', models.ForeignKey(blank=True, help_text='Logged-in-user', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='result.ASUBJECTS')),
                ('subject_by', models.ForeignKey(blank=True, help_text='subject_teacher', null=True, on_delete=django.db.models.deletion.CASCADE, to='result.BTUTOR')),
            ],
            options={
                'ordering': ('term',),
            },
        ),
        migrations.AddField(
            model_name='btutor',
            name='graded',
            field=models.ForeignKey(blank=True, help_text='Grade Counts', null=True, on_delete=django.db.models.deletion.CASCADE, to='result.RESULT_GRADE'),
        ),
        migrations.AddField(
            model_name='btutor',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='result.ASUBJECTS'),
        ),
        migrations.AddField(
            model_name='btutor',
            name='user',
            field=models.ForeignKey(blank=True, help_text='loggon-account:move account here', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='annual',
            name='student_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='result.CNAME'),
        ),
        migrations.AddField(
            model_name='annual',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='result.ASUBJECTS'),
        ),
        migrations.AddField(
            model_name='annual',
            name='subject_by',
            field=models.ForeignKey(blank=True, help_text='subject_teacher', null=True, on_delete=django.db.models.deletion.CASCADE, to='result.BTUTOR'),
        ),
    ]