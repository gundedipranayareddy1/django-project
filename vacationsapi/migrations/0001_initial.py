# Generated by Django 3.2.8 on 2021-10-19 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.CharField(max_length=7)),
                ('travel', models.BooleanField()),
                ('food', models.BooleanField()),
                ('accomodation', models.BooleanField()),
            ],
        ),
    ]
