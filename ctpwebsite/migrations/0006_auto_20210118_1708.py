# Generated by Django 3.1.5 on 2021-01-18 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ctpwebsite', '0005_auto_20210116_1409'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': '验证问题', 'verbose_name_plural': '验证问题'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AlterField(
            model_name='question',
            name='Question_enable',
            field=models.BooleanField(default=1, verbose_name='有效性'),
        ),
        migrations.AlterField(
            model_name='question',
            name='Question_question',
            field=models.CharField(max_length=40, verbose_name='验证问题'),
        ),
        migrations.AlterField(
            model_name='users',
            name='User_Questionid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='ctpwebsite.question', verbose_name='验证问题ID'),
        ),
        migrations.AlterField(
            model_name='users',
            name='User_answer',
            field=models.TextField(verbose_name='回答'),
        ),
        migrations.AlterField(
            model_name='users',
            name='User_enable',
            field=models.BooleanField(default=1, verbose_name='有效性'),
        ),
        migrations.AlterField(
            model_name='users',
            name='User_name',
            field=models.CharField(max_length=30, verbose_name='账号'),
        ),
        migrations.AlterField(
            model_name='users',
            name='User_password',
            field=models.CharField(max_length=128, verbose_name='密码'),
        ),
    ]
