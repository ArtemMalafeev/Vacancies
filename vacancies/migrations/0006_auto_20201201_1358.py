# Generated by Django 3.1.3 on 2020-12-01 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0005_auto_20201201_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(default='https://place-hold.it/100x60', upload_to='vacancies/images/'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.ImageField(default='https://place-hold.it/100x60', upload_to='specialties/images/'),
        ),
    ]
