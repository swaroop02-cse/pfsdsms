# Generated by Django 5.0.7 on 2024-10-08 15:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0006_alter_addcourse_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.AlterField(
            model_name='addcourse',
            name='course',
            field=models.CharField(choices=[('AOOP', 'ADVANCED OBJECT ORIENTED PROGRAMMING'), ('PFSD', 'PYTHON FULL STACK DEVELOPMENT')], max_length=50),
        ),
        migrations.AlterField(
            model_name='addcourse',
            name='section',
            field=models.CharField(choices=[('S11', 'SECTION S11'), ('S12', 'SECTION S12'), ('S13', 'SECTION S13'), ('S14', 'SECTION S14'), ('S15', 'SECTION S15'), ('S16', 'SECTION S16'), ('S17', 'SECTION S17')], max_length=50),
        ),
    ]
