from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.


def index(request):
    if request.method == 'POST': # Htmldeki formun methodu post ise :
        form = CommentForm(request.POST) # Methodu post olan formu çek
        if form.is_valid(): # Formdaki alanlar doğru girildiyse
            user_comment = form.save(commit=False) # Kayıt et ama yayınlama
            user_comment.user = request.user
            user_comment.save()
            return redirect('index') # Ve ilgili sayfayı tekrar çağır
        else:
            return render(request,'index.html',context)
        
    comment = Comment.objects.all() # Bir modelin içindeki her value değerini sayfaya göndermek için kullanırız.
    
    tersComment = reversed(comment)


    
    form = CommentForm()
    context = {
        'yorum':tersComment,
        'form':form,
    }
    return render(request,'index.html',context)


def sil(request):
    if request.method == 'POST': # Formun methodu post ise 
        silId = request.POST['silValue'] #Htmldeki inputtaki "name" değerini baz alarak idleri çektik
        silComment = Comment.objects.filter(id = silId) # Filter ile htmldeki ID ile veritabanında ID eşit olanı al
        silComment.delete()
        return redirect('index')
        

