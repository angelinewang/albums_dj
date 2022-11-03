from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_artist),
    path("list", views.ArtistsListView.as_view(), name="artist_list"),
    path("createlist", views.CreateListView.as_view(), name="create_artist"),
]
