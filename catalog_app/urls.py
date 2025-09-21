from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArtisteListView.as_view(), name='home'),  # Home page
    path('artistes/', views.ArtisteListView.as_view(), name='artiste_list'),
    path('artistes/<int:pk>/', views.ArtisteDetailView.as_view(), name='artiste_detail'),
    path('artistes/create/', views.ArtisteCreateView.as_view(), name='artiste_create'),
    path('artistes/<int:pk>/update/', views.ArtisteUpdateView.as_view(), name='artiste_update'),
    path('artistes/<int:pk>/delete/', views.ArtisteDeleteView.as_view(), name='artiste_delete'),
    path('songs/', views.SongListView.as_view(), name='song_list'),
    path('songs/<int:pk>/', views.SongDetailView.as_view(), name='song_detail'),
    path('songs/create/', views.SongCreateView.as_view(), name='song_create'),
    path('songs/<int:pk>/update/', views.SongUpdateView.as_view(), name='song_update'),
    path('songs/<int:pk>/delete/', views.SongDeleteView.as_view(), name='song_delete'),
    path('lyrics/', views.LyricListView.as_view(), name='lyric_list'),
    path('lyrics/<int:pk>/', views.LyricDetailView.as_view(), name='lyric_detail'),
    path('lyrics/create/', views.LyricCreateView.as_view(), name='lyric_create'),
    path('lyrics/<int:pk>/update/', views.LyricUpdateView.as_view(), name='lyric_update'),
    path('lyrics/<int:pk>/delete/', views.LyricDeleteView.as_view(), name='lyric_delete'),
]