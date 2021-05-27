from django.shortcuts import render, get_object_or_404

from .models import BlogPost
from .forms import BlogPostForm, BlogPostModelForm

# Create your views here.


def blog_list_page(request):
    template_name = 'blog/list.html'
    queryset = BlogPost.objects.all()
    context = {
        "obj_list":queryset,
        "title":"Blogs List"
    }
    return render(request, template_name, context)

def blog_detail_page(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {
        'obj':obj,
        'title':"Blog Detail"
    }
    return render(request, template_name, context)

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