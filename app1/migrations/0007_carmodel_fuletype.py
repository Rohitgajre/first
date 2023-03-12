# Generated by Django 3.2 on 2023-01-17 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_student_dept'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('fuletype', models.ManyToManyField(to='app1.FuleType')),
            ],
        ),
    ]
