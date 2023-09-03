# Generated by Django 4.2 on 2023-08-26 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obeapp', '0005_rename_uname_customuser_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='mid1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co', models.CharField(default='1', max_length=5)),
                ('courseoutcome', models.CharField(max_length=100)),
                ('knowledge_level', models.CharField(default='K1', max_length=5)),
                ('k1', models.CharField(max_length=50)),
                ('k2', models.CharField(max_length=50)),
                ('k3', models.CharField(max_length=50)),
                ('k4', models.CharField(max_length=50)),
                ('totalmarks', models.CharField(max_length=50)),
                ('course_code', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='mid2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co', models.CharField(default='1', max_length=5)),
                ('courseoutcome', models.CharField(max_length=100)),
                ('knowledge_level', models.CharField(default='K1', max_length=5)),
                ('k1', models.CharField(max_length=50)),
                ('k2', models.CharField(max_length=50)),
                ('k3', models.CharField(max_length=50)),
                ('k4', models.CharField(max_length=50)),
                ('totalmarks', models.CharField(max_length=50)),
                ('course_code', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='sem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co', models.CharField(default='1', max_length=5)),
                ('courseoutcome', models.CharField(max_length=100)),
                ('knowledge_level', models.CharField(default='K1', max_length=5)),
                ('k1', models.CharField(max_length=50)),
                ('k2', models.CharField(max_length=50)),
                ('k3', models.CharField(max_length=50)),
                ('k4', models.CharField(max_length=50)),
                ('totalmarks', models.CharField(max_length=50)),
                ('course_code', models.CharField(max_length=15)),
            ],
        ),
    ]