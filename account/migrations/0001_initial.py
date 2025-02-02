# Generated by Django 2.1.7 on 2019-08-30 19:56

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ANMUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anmuserlocalities', to='location.Locality')),
            ],
        ),
        migrations.CreateModel(
            name='ClusterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clusteruserscluster', to='location.Cluster')),
            ],
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.PositiveIntegerField()),
                ('otp', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParentUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('m_name', models.CharField(max_length=50)),
                ('f_dob', models.DateField()),
                ('m_dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='WardUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wardusers', to=settings.AUTH_USER_MODEL)),
                ('ward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wardusersward', to='location.Ward')),
            ],
        ),
        migrations.AddField(
            model_name='parentuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parentusers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='clusteruser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clusterusers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='anmuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anmusers', to=settings.AUTH_USER_MODEL),
        ),
    ]
