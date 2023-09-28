from rest_framework import serializers
from .models import Section, Menu


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('section',)


class MenuSerializer(serializers.ModelSerializer):
    section = serializers.SlugRelatedField(slug_field='section', queryset=Section.objects.all())

    class Meta:
        model = Menu
        fields = ('id', 'section', 'title', 'the_dish', 'price', 'weight', 'img')
