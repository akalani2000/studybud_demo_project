# Generated by Django 4.0.5 on 2022-07-24 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_bio_user_name_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='abc.jpg', null=True, upload_to=''),
        ),
    ]
