from . import models
import hashlib
from redis import StrictRedis
def check(uid,pwd):
    """用户登陆验证。"""

    objs=models.Users.objects.filter(User_name=uid)
    if len(objs)==0:
        return -1
    elif hashlib.md5(pwd.encode(encoding='UTF-8')).hexdigest()==objs[0].User_password:
        return 1
    else:
        return 0

def registerdb(uid,pwd,question,answer):
    """用户注册。"""
    
    objs=models.Users.objects.filter(User_name=uid)
    if  objs.exists()==False:
        password=hashlib.md5(pwd.encode(encoding='UTF-8')).hexdigest()
        q=models.Question.objects.filter(pk=int(question))[0]
        models.Users.objects.create(User_name=uid,User_password=password,question=q,User_answer=answer)
        return 1
    else:
        return 0

def getquestionlist():
    """返回验证问题字典"""
    result={}
    for qset in models.Question.objects.values('id','Question_question'):
        result[str(qset['id'])]=qset['Question_question']
    return result

def getkdata(id):
    redis=StrictRedis(decode_responses=True)
    result=redis.hgetall(id)
    redis.close()
    return result
