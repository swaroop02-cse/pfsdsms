# Generated by Django 5.0.7 on 2024-10-07 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0004_alter_addcourse_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcourse',
            name='section',
            field=models.CharField(choices=[('S3', 'Section3'), ('S1', 'Section1'), ('S4', 'Section4'), ('S2', 'Section2')], max_length=50),
        ),
    ]
