# Generated by Django 3.1.5 on 2021-01-16 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctpwebsite', '0002_remove_users_user_ff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='User_enable',
            field=models.BooleanField(default=1),
        ),
        migrations.AlterField(
            model_name='users',
            name='User_password',
            field=models.CharField(max_length=128),
        ),
    ]
