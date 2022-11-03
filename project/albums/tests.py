from django.test import TestCase
from django.urls import reverse
from .models import Album

# Create your tests here.

class AlbumTestCase(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.album = Album.objects.create(
        title="A good title",
        artist="An excellent artist",
        release_year=1990,
    )

  def test_album_content(self):
    self.assertEqual(self.album.title, "A good title")
    self.assertEqual(self.album.artist, "An excellent artist")
    self.assertEqual(self.album.release_year, 1990)

  def test_album_listview(self):
    response = self.client.get(reverse("album_list"))
    print(response)
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "An excellent artist")
    self.assertTemplateUsed(response, "albums/album_list.html")
