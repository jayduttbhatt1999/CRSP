# Generated by Django 4.1.7 on 2023-08-02 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0059_remove_collaborationnotification_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborationnotification',
            name='collaboration_post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.collaborationpost'),
            preserve_default=False,
        ),
    ]
