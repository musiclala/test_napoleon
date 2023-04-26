# Generated by Django 4.2 on 2023-04-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('password', models.CharField(max_length=30, verbose_name='Password')),
                ('surname', models.CharField(max_length=30, verbose_name='Surname')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('number_phone', models.CharField(max_length=11, verbose_name='Number Phone')),
                ('avatar', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Avatar')),
                ('companies', models.ManyToManyField(related_name='companies', to='napoleon.company')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
