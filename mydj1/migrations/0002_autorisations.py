# Generated by Django 4.2.5 on 2023-10-02 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydj1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autorisations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.CharField(max_length=100, verbose_name='Login')),
                ('pas', models.CharField(max_length=150, verbose_name='Password')),
                ('email', models.CharField(max_length=200, verbose_name='Login')),
            ],
        ),
    ]
