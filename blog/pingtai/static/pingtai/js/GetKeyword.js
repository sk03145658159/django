$=django.jQuery
$(function(){
    $("#id_c").on("change",function () {
        $.ajax({
            url:"/GetKeyword/",
            data:{c:$(this).val()},
            type:"post",
            success:function (e) {
                $("#id_k>option").detach()   //删除id_k下的option
                str=""
                for (i in e){
                    str+=`       <!--模板字符串-->
                        <option value="${i}">${e[i]}</option>
                    `
                }
                $("#id_k").html(str)
            }
        })
    })
})
