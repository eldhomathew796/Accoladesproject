from django.urls import path
from .import views
app_name ='user'


urlpatterns = [
    path('',views.home,name="home"),
    path('About/',views.aboutdetail,name="About"),
    path('digitalmarketing/',views.digitalmarketing,name="digitalmarketing"),
    path('webdevelopment/',views.webdevelopment,name="webdevelopment"),
    path('graphic/',views.graphic,name="graphic"),
    
    
    path('contact/',views.contact,name="contact"),
   
    path('clientindex/',views.clientindex,name="clientindex"),
    path('showclient/<int:id>',views.showclient,name="showclient"),
    path('editclient/<int:id>/',views.editclient,name="editclient"),
    path('deleteclient/<int:id>',views.deleteclient,name="deleteclient"),
    path('gallery',views.gallery,name="gallery"),
    path('login',views.stafflogin,name="login"),
    path('stafflogin',views.stafflogin,name="stafflogin"),
    path('edit',views.edit,name="edit"),
    path('popup',views.popup,name="popup"),
    
    
    
    
]
   