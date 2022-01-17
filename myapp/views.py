from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DeleteView
from django.db.models import F


class BlockPageView(ListView):
    model = Block
    template_name = 'index.html'
    paginate_by = 4


class SingView(DeleteView):
    model = Block
    template_name = 'single.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.view = F('view')+2
        self.object.save()
        self.object.refresh_from_db()
        return context


class CategoryView(ListView):
    template_name = 'index.html'
    allow_empty = True
    paginate_by = 2

    def get_queryset(self):
        return Block.objects.filter(category__slug=self.kwargs['slug'])


class TagView(ListView):
    template_name = 'index.html'
    model = Block
    paginate_by = 4

    def get_queryset(self):
        return Block.objects.filter(tag__slug=self.kwargs['slug'])


class SearchView(ListView):
    template_name = 'search.html'
    paginate_by = 1

    def get_queryset(self):
        return Block.objects.filter(title__icontains=self.request.GET.get('s'))


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context



















