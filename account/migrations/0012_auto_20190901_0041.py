# Generated by Django 2.1.5 on 2019-08-31 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_districtuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parentuser',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='location.Locality'),
        ),
    ]
