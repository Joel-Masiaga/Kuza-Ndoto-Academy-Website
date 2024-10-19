from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Post

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/list_posts.html'
    context_object_name = 'posts'
    paginate_by = 6  # Limit of posts per page

def get_queryset(self):
    return Post.objects.all().order_by('-date_posted')  # Ensure you fetch posts

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description', 'content', 'image']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('list_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'content', 'image']
    template_name = 'blog/update_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Simplified return statement
    
    def get_success_url(self):
        # Redirect to the post detail page after a successful update
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('list_posts')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
