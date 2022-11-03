from rest_framework import serializers
from .models import Album
from artists.serializers import ArtistSerializer
from artists.models import Artist

class AlbumSerializer(serializers.ModelSerializer):

    artist = ArtistSerializer()

    class Meta:
        model = Album
        fields = ("id", "title", "artist", "release_year",)

    def create(self, validated_data):
        artist_data = validated_data.pop("artist")
        (artist, _) = Artist.objects.get_or_create(**artist_data)

        album = Album.objects.create(**validated_data, artist=artist)
        return album

    def update(self, album, validated_data):
        album.title = validated_data.get("title", album.title)
        album.release_year = validated_data.get("release_year", album.release_year)

        artist_data = validated_data.pop("artist")
        artist = album.artist
        artist.name = artist_data.get("name", artist.name)

        album.save()
        artist.save()
        return album
