# Generated by Django 4.1.7 on 2023-03-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('dept', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('scholar', models.CharField(max_length=50)),
            ],
        ),
    ]
