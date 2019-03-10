#Django中的生命周期    请求=》请求1=》请求2=》...=》views函数前执行的函数1=》views函数前执行的函数2=》...=》views函数=》异常...=》异常2=》异常1=》响应..=》响应2=》响应1
#中间件
from django.utils.deprecation import MiddlewareMixin
class myMiddle(MiddlewareMixin):
    def process_resquest(self,request):
        print("请求1")     #发送请求时执行，不能有return
    def process_response(self,request,response):
        print('响应1')    #返回响应时执行，必须有return
        return response
    def process_view(self,request,callback,callback_args,callback_kwargs):
        print("process_view1")   #不能有return    执行views函数前执行的函数
        print(callback)
        print(callback_args)
        print(callback_kwargs)
    def process_exception(self, request, exception):
        print('异常1')
class myMiddle2(MiddlewareMixin):
    def process_resquest(self,request):
        print("请求2")     #不能有return     发送请求时
    def process_response(self,request,response):
        print('响应2')    #必须有return     返回响应
        return response
    def process_view(self,request,callback,callback_args,callback_kwargs):
        print("process_view2")   #不能有return    执行views函数前执行的函数
        print(callback)
        print(callback_args)
        print(callback_kwargs)
    def process_exception(self, request, exception):
        print('异常2')
#加入到settings的MIDDLEWARE中，将按序执行