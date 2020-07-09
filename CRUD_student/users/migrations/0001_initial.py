# Generated by Django 3.0.7 on 2020-07-06 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=120, verbose_name='Teacher Name')),
                ('teacher_initial', models.CharField(max_length=120, unique=True)),
                ('teacher_id', models.CharField(max_length=120, verbose_name='Teacher ID')),
                ('contact', models.CharField(max_length=120)),
                ('salary', models.FloatField()),
                ('designation', models.CharField(choices=[('Senior Lecturer', 'Senior Lecturer'), ('Lecturer', 'Lecturer'), ('Lecturer(RA)', 'Lecturer(RA)'), ('Lecturer(contractual)', 'Lecturer(contractual)')], max_length=120)),
                ('date_of_birth', models.DateField()),
                ('blood_group', models.CharField(choices=[('A (+ve)', 'A (+ve)'), ('A (-ve)', 'A (-ve)'), ('B (+ve)', 'B (+ve)'), ('B (-ve)', 'B (-ve)'), ('O (+ve)', 'O (+ve)'), ('O (-ve)', 'O (-ve)'), ('AB (+ve)', 'AB (+ve)'), ('AB (-ve)', 'AB (-ve)')], max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('religion', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('std_name', models.CharField(max_length=120, verbose_name='Student Name')),
                ('std_id', models.CharField(max_length=120, primary_key=True, serialize=False, verbose_name='Student ID')),
                ('contact', models.CharField(max_length=120)),
                ('date_of_birth', models.DateField(null=True)),
                ('blood_group', models.CharField(choices=[('A (+ve)', 'A (+ve)'), ('A (-ve)', 'A (-ve)'), ('B (+ve)', 'B (+ve)'), ('B (-ve)', 'B (-ve)'), ('O (+ve)', 'O (+ve)'), ('O (-ve)', 'O (-ve)'), ('AB (+ve)', 'AB (+ve)'), ('AB (-ve)', 'AB (-ve)')], max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('religion', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]