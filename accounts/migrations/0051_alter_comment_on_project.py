# Generated by Django 4.1.7 on 2023-07-22 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0050_remove_post_keywords_comment_on_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='on_project',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]