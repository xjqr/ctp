$(function(){ 
    var c=drawcode();
    $("#code").click(function(){
       c=drawcode();
    });
    $("form").validate({
        rules:{
            uid:{required:true},
            pwd:{required:true,minlength:8},
            confirmpwd:{required:true,equalTo:"#pwd"},
            answer:{required:true},
        },
        messages:{
            uid:{required:"请输入账号"},
            pwd:{required:"请输入密码",minlength:"密码长度不能少于8个字符"},
            confirmpwd:{required:"请输入确定密码",equalTo:"两次密码不一致"},
            answer:{required:"请输入问题答案"},
        },
        errorElement:"em",
        onsubmit:true,
        submitHandler:function(form){
            if($("#checkcode").val().toLowerCase()!=c.toLowerCase()){
                alert('验证码错误！');
                return;
            }
            $("#checkstatus").val("b326b5062b2f0e69046810717534cb09");
            $.ajax({
                url:"/register/",
                type:"post",
                dataType:"json",
                data:$("form").serialize(),
                success:function(res){
                    if(res.isexist==0){
                        alert('该账号已存在，请修改账号！');
                        $("#uid").val()=="";
                    }else{
                        alert('注册成功');
                        window.location.href="/logic/";
                    }
                }
            });
        }
    });
});

function GetRandomCode(min,max){
    return Math.trunc(Math.random()*(max-min)+min);
}
function GetCheckCode(){
    var modes=Array(4);
    var code="";
    for(var i=0;i<4;i++){
        modes[i]=GetRandomCode(0,3)
    }
    for(var j=0;j<modes.length;j++){
        if(modes[j]==0){
            code+=String.fromCharCode(GetRandomCode(65,91));
        }
        if(modes[j]==1){
            code+=String.fromCharCode(GetRandomCode(97,123));
        }
        if(modes[j]==2){
            code+=String.fromCharCode(GetRandomCode(48,55));
        }
    }
    return code;
}
function drawcode(){
    var c=document.getElementById("code");
    var cax=c.getContext("2d");
    c.height=c.height;
    cax.fillStyle='white';
    cax.font='80pt Arial';
    var codestring=GetCheckCode();
    cax.fillText(codestring,20,90);
    return codestring;
}