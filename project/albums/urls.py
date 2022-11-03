from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_album),
    path("list", views.AlbumListView.as_view(), name="album_list"),
    path("createlist", views.CreateListView.as_view(), name="create_album"),
    path("<int:pk>", views.RUDView.as_view(), name="rud_album")
]