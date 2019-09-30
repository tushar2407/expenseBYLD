from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView,
    LogoutView as Logout,
    TemplateView
)
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.models import User
from main import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from services.infoget2 import returns
from services.UnderConstruction import returns1
# Create your views here.
class SignUp(LoginView):
    template_name='main/inputs1.html'
    def post(self,request):
        mobile=request.POST['username']
        #email=request.POST['user']
        password=request.POST['password']
        re_password=request.POST['re_password']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        month_limit=request.POST['month_limit']
        context={
            "username":mobile,
            "password":password, 
            #"email":email,
            "first_name":first_name,
            "month_limit":month_limit
        }
        if password == re_password:
            user=User.objects.create_user(username,first_name=first_name,email=email,password=password,month_limit=month_limit)
            user.save()
            redirect_authenticated_user= True
            return render(request, self.template_name, context)
        else :
            return HttpResponseBadRequest('Paswords do not match')
class Index(TemplateView):
    template_name='main/index.html'
    redirect_authenticated_user= True

class Logout(Logout):
    next_page='/'
class Inputs1(TemplateView):
    template_name='main/inputs1.html'

class Inputs(TemplateView):
    template_name='main/inputs.html'
    def get(self,request):
        sum=returns1()
        context={
            'sum':sum
        }
        return render(request,self.template_name,context)    
class Web(TemplateView):
    template_name='main/web.html'
    #context_object_name='file'
    def get(self, request, *args, **kwargs):
        content=returns()
        #content=content.remove(None)
        #text=str(text)
        context={
            "content":content,
           # "text":text
        }

       # print(context['content'][0][1])
        print(type(content[0]))
        print(content[0])
        return render(request, self.template_name,context)
class Web2(TemplateView):
    template_name='main/web2.html'

class Encrypt(TemplateView):
    template_name='main/encrypt.html'
    
class Contact(TemplateView):
    template_name='main/contact.html'