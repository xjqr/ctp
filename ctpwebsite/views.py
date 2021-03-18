from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
import json
from . import models
from django.forms.models import model_to_dict
from .BLL import *
from django.views.decorators.clickjacking import xframe_options_exempt
# Create your views here.

def logic(request):
    """用户登陆视图。"""
    if request.method=='GET':
        return render(request,'logic.html')
    if request.method=='POST':
        res=check(request.POST['uid'],request.POST['pwd'])
        if res==1:
            request.session.set_expiry(0) 
            request.session['user']=request.POST['uid']
            

        return HttpResponse(res)


def home(request):
    """主页视图。"""
    if request.method=='GET':
        if request.session.get('user',default=False):
            return render(request,'home.html')
        else:
            return redirect(to='/logic/')
    if request.method=='POST':
        if request.session.get('user',default=False):
            return HttpResponse({'a':'123','b':'456'})
        else:
            return redirect(to='/logic/')
        

def register(request):
    """用户注册视图。"""
    if request.method=='GET':
        return render(request,'register.html',context={'questionlist':getquestionlist()})
    if request.method=='POST':
        if request.POST['checkstatus']=="b326b5062b2f0e69046810717534cb09":            
            result=registerdb(request.POST['uid'],request.POST['pwd'],request.POST['question'],request.POST['answer'])
            res={'isexist':result}
            return JsonResponse(res)
        else:
            return HttpResponse('<p>未经许可本站禁止采集数据！</p>',status=404)

@xframe_options_exempt
def kpicture(request):
    # if request.session.get('user',default=False):
    #     return render(request,'kpicture.html')
    # else:
    #     return HttpResponse('<p>未经许可本站禁止采集数据！</p>',status=404)
     return render(request,'kpicture.html')

def kdataapi(request,id):
    if request.session.get('user',default=False):
        result=getkdata(id)
        return JsonResponse(result)
    

def logicout(request):
    """退出视图。"""
    request.session.clear()
    return redirect(to='/logic/')


def personcenter(request):
    """个人中心视图。"""
    if request.session.get('user',default=False):
        
        return render(request,'personcenter.html')
    