from django.urls import path
from . import views

urlpatterns = [
    path('',views.logic,name='logic'),
    path(r'logic/',views.logic,name='logic'),
    path(r'home/',views.home,name='home'),
    path(r'register/',views.register,name='register'),
    path(r'kpicture/',views.kpicture,name='kpicture'),
    path(r'logicout/',views.logicout,name='logicout'),
    path(r'kdataapi/<id>/',views.kdataapi,name='kdataapi'),
    path(r'personcenter/',views.personcenter,name='personcenter'),
    path(r'setting/',views.setting,name='setting'),
]

app_name='ctpwebsite'