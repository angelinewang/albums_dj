# Generated by Django 4.1.2 on 2022-10-29 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('artist', models.CharField(max_length=250)),
                ('year_of_release', models.IntegerField()),
            ],
        ),
    ]
