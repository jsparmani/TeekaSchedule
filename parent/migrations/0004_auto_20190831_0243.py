# Generated by Django 2.1.7 on 2019-08-30 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parent', '0003_vaccinationdata_vaccine'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vaccinationdata',
            options={'ordering': ['duration']},
        ),
    ]
