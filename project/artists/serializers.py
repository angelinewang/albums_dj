from rest_framework import serializers
from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ("id", "name",)

    def create(self, validated_data):

        artist = Artist.objects.create(**validated_data)
        return artist

    def update(self, artist, validated_data):
        artist.name = validated_data.get("name", artist.name)

        artist.save()
        return artist
