from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),    
    path('saveenquiry/',views.saveenquiry,name='saveenquiry'),    
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),    
    path('logout/',views.log_out,name='log_out'),    

]
