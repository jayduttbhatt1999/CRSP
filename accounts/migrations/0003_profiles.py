# Generated by Django 4.1.7 on 2023-03-21 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_password_alter_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('dept', models.CharField(max_length=50)),
                ('scholar', models.CharField(max_length=50)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
    ]
