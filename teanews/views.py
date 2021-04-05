from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.

def teanews_home(request):
    news = Article.objects.order_by('-created_at')
    return render(request, 'teanews/teanews_home.html', {'news':news})

class NewsDetailView(DetailView):
    model = Article
    template_name = 'teanews/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'teanews/create_text.html'
    form_class = ArticleForm


class NewsDeleteView(DeleteView):
    model = Article
    success_url = '/teanews'
    template_name = 'teanews/teanews_delete.html'


def create_text(request):

    if request.method == "POST":
        # error = ''
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teanews_home')
        # else:
        #     error = "Форма не вірна"

    form = ArticleForm()
    form_dictionary = {
        'form': form,
        # 'error': error
    }
    return render(request, 'teanews/create_text.html', form_dictionary)