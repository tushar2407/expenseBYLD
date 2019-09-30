from django.urls import path
from main import views
from django.contrib.auth.decorators import login_required

urlpatterns=[
    #path('page1/', views.page1, name='page1'),
    path('', views.Index.as_view(),name='index'),
    path('inputs',views.Inputs.as_view(), name='inputs'),
    path('inputs1',views.Inputs1.as_view(),name='inputs1'),
    path('web',views.Web.as_view(), name='web'),
    path('web2',views.Web2.as_view(), name='web2'),
    path('/',views.Logout.as_view(),name='logout'),
    path('contact',views.Contact.as_view(),name='contact'),
   # path('encrypt_file',views.Encrypt_file.as_view(), name='encrypt_file'),
    #path('signup', views.SignUp.as_view(), name='signup')
    path('logout/', views.Index.as_view())
   #path('encrypt',views.encrypt)

]