# Generated by Django 5.1.7 on 2025-03-13 03:46

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_unit_name', models.CharField(max_length=100)),
                ('course_unit_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=100)),
                ('course_units', models.ManyToManyField(related_name='course_units', to='AITS.courseunit')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('password2', models.CharField(max_length=20)),
                ('Role', models.CharField(choices=[('Student', 'STUDENT'), ('Lecturer', 'LECTURER'), ('Academic_registrar', 'ACADEMIC REGISTRAR')], default='Student', max_length=40)),
                ('Gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE')], max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('year_of_study', models.CharField(choices=[('YEAR 1', 'YEAR 1'), ('YEAR_2', 'YEAR 2'), ('YEAR_3', 'YEAR 3'), ('YEAR_4', 'YEAR 4'), ('YEAR_5', 'YEAR 5')], max_length=20, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='AITS.program')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(default='Semester 1', max_length=30)),
                ('issue_type', models.CharField(choices=[('missing_marks', 'MISSING MARKS'), ('appeal', 'APPEAL'), ('correction', 'CORRECTION')], max_length=50)),
                ('issue_status', models.CharField(choices=[('Pending', 'PENDING'), ('Resolved', 'RESOLVED'), ('In Progress', 'IN PROGRESS')], default='Pending', max_length=50)),
                ('issue_description', models.TextField()),
                ('Image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('course_unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AITS.courseunit')),
                ('lecturer', models.ForeignKey(limit_choices_to={'Role': 'Lecturer'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lecturer_issues', to=settings.AUTH_USER_MODEL)),
                ('registrar', models.ForeignKey(limit_choices_to={'Role': 'Academic_registrar'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='registrar_issues', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(limit_choices_to={'Role': 'Student'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issues', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['update', 'date_created'],
            },
        ),
    ]
