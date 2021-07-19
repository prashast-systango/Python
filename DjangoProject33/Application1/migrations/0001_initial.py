# Generated by Django 2.2.12 on 2021-07-16 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=40)),
                ('roll_no', models.IntegerField(unique=True)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
