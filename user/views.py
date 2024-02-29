from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.


def user_login(request):
    form = UyeGirisForm(request,data = request.POST)
    
    
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                next_url = request.GET.get('next',None)
                messages.success(request,'Giriş Başarılı')
                if next_url is None:
                    
                    return redirect('index')
                else:
                    
                    return redirect (next_url)
            
            
        else:
            messages.error(request,'Giriş Başarısız Kullancı Adı veya şifreyi kontrol ediniz ! ')
            return render(request,'login.html',{'form':form})

    form = UyeGirisForm()
    return render(request,'login.html',{'form':form})


def user_logout(request):
    logout(request)
    return redirect('login')


def user_register(request):
    if request.method == 'POST':
        form = UyeKayitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'register.html',{'form':form})
        
    form = UyeKayitForm()
    
    return render(request,'register.html',{'form':form})



def sifre_degistir(request):
    if request.method == 'POST':
        form = SifreDegistir(request.user,request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request,'sifreDegis.html',{'form':form})
        
    form = SifreDegistir(request.user)
   
    return render(request,'sifreDegis.html',{'form':form})


