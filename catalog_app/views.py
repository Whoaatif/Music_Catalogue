import logging
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import Artiste, Song, Lyric
from .forms import ArtisteForm, SongForm, LyricForm

logger = logging.getLogger(__name__)

# Artiste Views
class ArtisteListView(ListView):
    model = Artiste
    template_name = 'catalog_app/artiste_list.html'
    context_object_name = 'artistes'

class ArtisteDetailView(DetailView):
    model = Artiste
    template_name = 'catalog_app/artiste_detail.html'

class ArtisteCreateView(CreateView):
    model = Artiste
    form_class = ArtisteForm
    template_name = 'catalog_app/artiste_form.html'
    success_url = reverse_lazy('artiste_list')

class ArtisteUpdateView(UpdateView):
    model = Artiste
    form_class = ArtisteForm
    template_name = 'catalog_app/artiste_form.html'
    success_url = reverse_lazy('artiste_list')

class ArtisteDeleteView(DeleteView):
    model = Artiste
    # template_name = 'catalog_app/artiste_confirm_delete.html' # Removed for AJAX
    success_url = '/artistes/'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        logger.info(f"Deleting Artiste: {self.object}")
        self.object.delete()
        return JsonResponse({'success': True})

# Song Views
class SongListView(ListView):
    model = Song
    template_name = 'catalog_app/song_list.html'
    context_object_name = 'songs'

class SongDetailView(DetailView):
    model = Song
    template_name = 'catalog_app/song_detail.html'

class SongCreateView(CreateView):
    model = Song
    form_class = SongForm
    template_name = 'catalog_app/song_form.html'
    success_url = reverse_lazy('song_list')

class SongUpdateView(UpdateView):
    model = Song
    form_class = SongForm
    template_name = 'catalog_app/song_form.html'
    success_url = reverse_lazy('song_list')

class SongDeleteView(DeleteView):
    model = Song
    # template_name = 'catalog_app/song_confirm_delete.html' # Removed for AJAX
    success_url = '/songs/'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        logger.info(f"Deleting Song: {self.object}")
        self.object.delete()
        return JsonResponse({'success': True})

# Lyric Views
class LyricListView(ListView):
    model = Lyric
    template_name = 'catalog_app/lyric_list.html'
    context_object_name = 'lyrics'

class LyricDetailView(DetailView):
    model = Lyric
    template_name = 'catalog_app/lyric_detail.html'

class LyricCreateView(CreateView):
    model = Lyric
    form_class = LyricForm
    template_name = 'catalog_app/lyric_form.html'
    success_url = reverse_lazy('lyric_list')

class LyricUpdateView(UpdateView):
    model = Lyric
    form_class = LyricForm
    template_name = 'catalog_app/lyric_form.html'
    success_url = reverse_lazy('lyric_list')

class LyricDeleteView(DeleteView):
    model = Lyric
    # template_name = 'catalog_app/lyric_confirm_delete.html' # Removed for AJAX
    success_url = '/lyrics/'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        logger.info(f"Deleting Lyric: {self.object}")
        self.object.delete()
        return JsonResponse({'success': True})
