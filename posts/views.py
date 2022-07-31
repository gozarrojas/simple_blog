from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy
# Models
from posts.models import Post
from categories.models import Category
from comments.models import Comment
from comments.forms import CreateCommentForm


class PostsFeedView(ListView):
    template_name = 'posts/index.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 5
    # Esto es lo que retorna
    context_object_name = 'posts'

    # Voy a retornar el listado siempre y cuando no se un borrador
    def get_queryset(self):
        return Post.objects.filter(is_draft=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


# DetailView recupera información en concreto
class PostDetailView(DetailView):
    """Detail post."""
    template_name = 'posts/detail.html'
    model = Post
    context_object_name = 'post'
    slug_field = 'url'
    slug_url_kwarg = 'url'

    def get_queryset(self):
        return Post.objects.filter(is_draft=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['comments'] = Comment.objects.filter(post=self.get_object()).all()
        context['form_comments'] = CreateCommentForm()
        return context


class AddPostView(CreateView):
    template_name = 'posts/add.html'
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('posts:blog')


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'posts/update.html'
    fields = '__all__'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts:blog')


@login_required
def save_comment(request):
    if request.method == 'POST':
        url = request.POST['url']
        post = {
            'user': request.user.id,
            'profile': request.user.id,
            'comment': request.POST['comment'],
            'post': request.POST['post']
        }
        form = CreateCommentForm(post)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', url=url)
    else:
        return HttpResponse(status=405)
    return HttpResponse(status=500)
