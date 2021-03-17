function logic(){
    if($("#uid").val()==''||$('#pwd').val()==''){
        alert('用户名或密码不能为空');
    }
    else{
        $.ajax({
            url:"/logic/",
            type:"post",
            dataType:"html",
            data:$('#form_userinfo').serialize(),
            success:function(data){
                if(data==-1){
                    alert('该用户不存在!');
                }
                else if (data==0){
                    alert('用户名或密码错误!');
                }
                else if(data==1){
                   window.location.href='/home/';
                }
            },
        });
    }
}
function gotoregisterpage(){
    window.location.href='/register/';
}