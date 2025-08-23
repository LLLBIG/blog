from django.shortcuts import render
from django.http.response import HttpResponseBadRequest
from libs.captcha.captcha import captcha

# Create your views here.
#注册视图
class RegisterView:
    def get(self,request):
        return render(request,'register.html')
class ImageCodeView(View):
    def get(self,request):
        uuid = request.GET.get("uuid")
        if uuid is None:
            return HttpResponseBadRequest("没有传递uuid")
        text,image = captcha.generate_captcha()

        pass