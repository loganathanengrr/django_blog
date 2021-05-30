from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm, BlogPostModelForm

# Create your views here.


@login_required
def blog_list_page(request):
    template_name = 'blog/list.html'
    queryset = BlogPost.objects.all()
    context = {
        "obj_list":queryset,
        "title":"Blogs List"
    }
    return render(request, template_name, context)

@login_required()
def blog_detail_page(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {
        'obj':obj,
        'title':"Blog Detail"
    }
    return render(request, template_name, context)

@login_required()
def blog_create_view(request):
    form =  BlogPostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        print(obj.content)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    template_name = 'blog/form.html'
    context = {
        "title":"Create Post",
        "form" :form
            
    }
    return render(request, template_name, context)

@login_required
def blog_update_view(request, slug):
    obj =  get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = BlogPostForm()
    title = f"Upate {obj.title}"
    context = {
        "form":form,
        "title": title
    }
    template_name = "blog/form.html"
    return render(request, template_name, context)

@login_required
def blog_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        obj.delete()
        return redirect('/blog')
    context = {"obj" : obj}
    template_name = "blog/delete.html"
    return render(request, template_name, context)

    
