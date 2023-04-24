from django.shortcuts import render,redirect
from .models import slider,About,digitalmarketingservice,webdevelopmentservice,graphicdesigning,Gallery,galleryaccola,Clients
from .forms import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login
# Create your views here.
def home(request):
    sliders=slider.objects.all()
    return render(request,'home.html',{'slider':sliders})

def aboutdetail(request):
    abouts=About.objects.all()
    return render(request,'about.html',{'about':abouts})

def digitalmarketing(request):
    dmng=digitalmarketingservice.objects.all()
    return render(request,'digitalmarketing.html',{'dmng':dmng})

def webdevelopment(request):
    web=webdevelopmentservice.objects.all()
    return render(request,'webdevelopment.html',{'web':web})

def graphic(request):
    gra=graphicdesigning.objects.all()
    return render(request,'graphicdesigning.html',{'gra':gra})

def login(request):
    return render(request,'login.html')
def edit(request):
    return render(request,'edit.html')

def popup(request):
    return render(request,'popup.html')






def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['number']
        message=request.POST['message']
        clients=Clients(name=name, email=email, number=number, message=message)
        clients.save()
        # return redirect('home')
    return render(request,'contact.html')


def clientindex(request):

    obj=Clients.objects.all()
    
    return render(request,'clientindex.html',{'i_obj':obj})

def showclient(request,id):
    cli=Clients.objects.get(id=id)
    context={
        'cli':cli
    }
    return render(request,'showclient.html',context)

def editclient(request,id):
    clients=Clients.objects.get(id=id)
    form =ClientsForm(request.POST or None, request.FILES, instance=clients)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'editclient.html',{'form':form,'cli':clients})

def deleteclient(request,id):
    clients=Clients.objects.get(id=id)
    clients.delete()
    return redirect('/')
   
   
    


def gallery(request):
    gall=galleryaccola.objects.all()
    return render(request,'gallery.html',{'gall':gall})

def stafflogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            if user.is_superuser:
                auth.login(request,user)
                return redirect('user:clientindex')
            else:
                #   login(request,user)
                #   auth.login(request,user)
                 messages.info(request,'Invalid username and password')
                 return redirect('clientindex')
                    # return redirect('userhomepage')
            
                
    else:
        return render(request,'login.html')
    
        
        

