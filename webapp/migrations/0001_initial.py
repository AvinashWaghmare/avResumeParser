# Generated by Django 3.0.4 on 2020-03-30 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='resumes/', verbose_name='Upload Resumes')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Email')),
                ('mobile_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Mobile Number')),
                ('education', models.CharField(blank=True, max_length=255, null=True, verbose_name='Education')),
                ('skills', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Skills')),
                ('company_name', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Company Name')),
                ('college_name', models.CharField(blank=True, max_length=1000, null=True, verbose_name='College Name')),
                ('designation', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Designation')),
                ('experience', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Experience')),
                ('uploaded_on', models.DateTimeField(auto_now_add=True, verbose_name='Uploaded On')),
                ('total_experience', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Total Experience (in Years)')),
            ],
        ),
    ]
