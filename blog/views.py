from django.shortcuts import redirect, render , HttpResponse
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.


def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request, 'blog/blogPost.html', context)

@login_required(login_url='/login')
def new(request):
    if request.method == 'POST':
        import string    
        import random
        slugRan = str(''.join(random.choices(string.ascii_lowercase + string.digits, k = 10)))
        title = request.POST['title']
        content = request.POST['content'].replace('\n', '<br>')
        author = request.user
        date = request.POST['date']
        time = request.POST['time']
        Fslugval = title,slugRan
        slugval = Fslugval
        fslug=''
        for index, char in enumerate(slugval):
            if char == slugval[-1]:
                    if not(slugval[index] == " "):
                        fslug = fslug + char
            elif not(slugval[index] == " " and slugval[index+1]==" "):                        
                fslug = fslug + char
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        slug=''
        for char in fslug:
            if char not in punctuations:
                slug = slug + char
        slug = slug.replace(' ', '-')

        newPost = Post(title = title, content=content, author=author, slug=slug, timeStamp=time, DateStamp=date)
        newPost.save()
        messages.success(request, 'Your new Blog Post')
        return redirect('/blog/'+slug)
    return render(request, 'blog/new.html')

def deletepost(request):
    if request.method == 'POST':
        dSlug=request.POST['Dslug']
        Post.objects.filter(slug=dSlug).delete()
        messages.success(request, 'Deleted Successfully!')
        return redirect('/dashboard')
    return redirect('/dashboard')

def editpost(request):
    if request.method == 'POST':
        Eslug = request.POST['Eslug']
        Epost = Post.objects.filter(slug=Eslug).first()
        print(Epost)
        context = {'post':Epost}
        print(Eslug)
        return render(request, 'blog/editPost.html', context)
    return render(request, 'blog/editPost.html')

def update(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content'].replace('\n', '<br>')
        slug = request.POST['slug']
        date = request.POST['date']
        time = request.POST['time']
        Epost = Post.objects.filter(slug=slug).update(title = title, content=content, timeStamp=time, DateStamp=date)
        messages.success(request, 'Updated Successfully!!')
        return redirect('/blog/'+slug)
    return redirect('new')