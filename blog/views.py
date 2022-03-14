from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.generics import get_object_or_404
from django.utils import timezone
from blog.models import Post
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from .forms import FeedbackForm

index = never_cache(TemplateView.as_view(template_name='blog/post_list.html'))

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:3]
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('feedback/')
        else:
            return redirect('blank_feedback/')
           
    else:
        f = FeedbackForm()
        return render(request, 'blog/post_list.html', {'posts': posts, 'form': f})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/article.html', {'post': post})
    
def test_redirect(request):
    c = Category.objects.get(name='python')
    return redirect(c)
 
def feedback(request):
    return render(request, 'blog/feedback.html')
    #return redirect('blog/feedback.html')

def blank_feedback(request):
    return render(request, 'blog/feedback2.html')
