from django.db import models

# Create your models here.

class Question(models.Model):
    Question_question=models.CharField(max_length=40,verbose_name=u'验证问题')
    Question_enable=models.BooleanField(default=1,verbose_name=u'有效性')
    class Meta:
        verbose_name=u'验证问题'
        verbose_name_plural=u'验证问题'



def set_default():
    resid=Question.objects.count()
    return resid

class Users(models.Model):
    User_name=models.CharField(max_length=30,verbose_name='账号',unique=True)
    User_password=models.CharField(max_length=128,verbose_name='密码')
    User_enable=models.BooleanField(default=1,verbose_name='有效性')
    question=models.ForeignKey(to=Question,on_delete=models.DO_NOTHING,default=set_default(),verbose_name='验证问题ID')
    User_answer=models.TextField(verbose_name='回答')
    class Meta:
        verbose_name=u'用户'
        verbose_name_plural=u'用户'

class Ctp_File(models.Model):
    code=models.CharField(max_length=20,verbose_name="合约代码")
    isfininsh=models.BooleanField(default=0,verbose_name="完成")
    filelen=models.CharField(max_length=30,verbose_name="文件大小")
    class Meta:
        verbose_name=u'文件'
        verbose_name_plural=u'文件'
    


    





