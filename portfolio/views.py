from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.models import Contact, Blogs

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        query = Contact(name=name, email=email, phonenumber=phone, description=desc)
        query.save()
        messages.success(request,"Thanks for conatacting! Your message has been sent successfully.")
        # print(name, email, phone, desc)
        return redirect('/')
    
    return render(request, 'contact.html')

def blog(request):
    posts = Blogs.objects.all()
    context = {'posts':posts}
    return render(request, 'handleblog.html', context=context)
# 6:11:4