# Generated by Django 4.2 on 2023-07-27 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obeapp', '0002_userform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
                ('department_id', models.CharField(max_length=100)),
                ('department_hod_name', models.CharField(max_length=200)),
                ('department_hod_id', models.CharField(max_length=100)),
            ],
        ),
    ]
