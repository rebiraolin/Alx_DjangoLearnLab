from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy, reverse
from .models import Post, Comment
from .forms import PostForm, CommentForm


# Create your views here.

def register(request):
    form = UserRegistrationForm()

    context = {'form': form}

    if request.method == 'GET':
        return render(request, 'blog/register.html', context)

    elif request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'GET':
        form = UserUpdateForm(instance=request.user)
        context = {'form': form}
        return render(request, 'blog/profile.html', context)
    elif request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
        else:
            return render(request, 'blog/profile.html', {'form': form})


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comment_set.all().order_by('-created_at')
        context['comment_form'] = CommentForm()

        return context
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = self.request.user
            comment.save()
            return redirect('post_detail', pk=self.object.pk)
        return self.get(request, *args, **kwargs)



class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog_home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'


    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        comment = self.get_object()
        return reverse('post_detail', kwargs={'pk':comment.post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin , DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    def get_success_url(self):
        comment = self.get_object()
        return reverse('post_detail', kwargs={'pk':comment.post.pk})

    def get_object(self, queryset=None):
        comment_pk = self.kwargs.get('pk')
        post_pk = self.kwargs.get('post_pk')
        comment = get_object_or_404(Comment, pk=comment_pk, post__pk=post_pk)
        return comment




