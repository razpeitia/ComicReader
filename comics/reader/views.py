from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.views import login
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from braces.views import LoginRequiredMixin

from .models import Comic
from .models import Page


def custom_login(request, *args, **kwargs):
    if request.user.is_authenticated():
        return redirect('reader:comic_list')
    else:
        return login(request, *args, **kwargs)


class ComicBookListView(LoginRequiredMixin, ListView):
    model = Comic
    template_name = 'reader/comic_list.html'
    context_object_name = 'comic_list'
comic_list = ComicBookListView.as_view()


class ComicBookDetailView(LoginRequiredMixin, DetailView):
    model = Comic
    queryset = Comic.objects.select_related()
    template_name = 'reader/comic_detail.html'
    context_object_name = 'comic'
comic_detail = ComicBookDetailView.as_view()

@login_required
def page(request, slug, issue, number):
    template_name = 'reader/page.html'
    page = get_object_or_404(Page, page_number=number, issue__number=issue, issue__comic__slug=slug)
    return render(request, template_name, {'page': page})