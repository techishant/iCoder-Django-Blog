from blog.models import Post
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from home.models import Contact
from django.contrib import auth
from blog.models import Post
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Ishant
# ish@0101
# Abhinav
# abhinav@sharma

def home(request):
    allPost= Post.objects.all()
    context = {'fpost': allPost}
    return render(request, 'home/home.html', context)
def about(request):
    return render(request, 'home/about.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']    
        email = request.POST['email']    
        fName = request.POST['fName']    
        lName = request.POST['lName']    
        password = request.POST['password']
        if len(password)<8:
            messages.error(request, "Account Can't be created")
            return redirect('/register')
        else:
            newUser = User.objects.create_user(username, email, password)
            newUser.last_name = lName  
            newUser.first_name = fName
            newUser.save()
            messages.success(request, 'Account Created Successfull!! Login Now')
            return redirect('/login')  
    return render(request, 'register.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'logged in successfully!!')
            return redirect('/')
        else:
            messages.error(request, 'Unable to login. Try again')
            return render(request, 'login.html')
    return render(request, 'login.html')

@login_required(login_url='/login')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Fill Form Properly")
        else:
            print(name, email, phone, content)
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Message Sent Successfully!")
    return render(request, 'home/contact.html')

def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logged out Successfully!!')
        return redirect('/')
    return redirect('/')

def dashboard(request):
    post = Post.objects.filter(author = request.user).all()
    context = {'allposts':post}
    return render(request, 'home/dashboard.html',context)