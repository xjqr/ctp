# Generated by Django 3.1.5 on 2021-01-18 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctpwebsite', '0006_auto_20210118_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='User_Questionid',
            new_name='Question',
        ),
    ]