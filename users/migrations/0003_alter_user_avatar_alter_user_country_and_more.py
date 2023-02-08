# Generated by Django 4.1.6 on 2023-02-08 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_username_alter_user_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='аватарка'),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='страна'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='телефон'),
        ),
    ]
