# Generated by Django 4.1.7 on 2023-07-05 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0047_alter_comment_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='reply',
            new_name='reply_content',
        ),
    ]
