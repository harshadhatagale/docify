from rest_framework import serializers
from .models import Project
from .models import Page
from .models import Section


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields=[
            "id",
            'name',
            'slug',
            'description',
            'is_visible',
            'created_at',
            'updated_at'
        ]
        read_only_fields= ['id','created_at','updated_at']

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Section
        fields=[
            "id",
            'name',
            'slug',
            'position',
            'created_at',
            'updated_at'
        ]
        read_only_fields= ['id','created_at','updated_at']

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model= Page
        fields=[
            "id",
            'title',
            'slug',
            'description',
            'position',
            "is_published",
            'created_at',
            'updated_at'
        ]
        read_only_fields= ['id','created_at','updated_at']

class PublicPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "position",
        ]


class PublicSectionSerializer(serializers.ModelSerializer):
    pages = PublicPageSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Section
        fields = [
            "id",
            "name",
            "slug",
            "position",
            "pages",
        ]


class PublicProjectSerializer(serializers.ModelSerializer):
    sections = PublicSectionSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "sections",
        ]