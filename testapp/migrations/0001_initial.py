# Generated by Django 5.0.1 on 2024-04-20 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('english', models.IntegerField()),
                ('sanskrit', models.IntegerField()),
                ('maths1a', models.IntegerField()),
                ('maths1b', models.IntegerField()),
                ('physics', models.IntegerField()),
                ('chemistry', models.IntegerField()),
            ],
        ),
    ]
