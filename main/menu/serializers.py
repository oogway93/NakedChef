from rest_framework import fields, serializers

from .models import Section, Menu


class MenuSerializer(serializers.ModelSerializer):
    section = serializers.SlugRelatedField(slug_field='section', queryset=Section.objects.all())

    class Meta:
        model = Menu
        fields = ('id', 'section', 'title', 'the_dish', 'price', 'weight', 'img')