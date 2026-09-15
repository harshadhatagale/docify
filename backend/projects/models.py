from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    owner= models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="projects"
    )
    name= models.CharField(max_length=255)
    slug= models.SlugField(unique=True)
    is_visible= models.BooleanField(default=False)
    description= models.TextField(blank=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

class Section(models.Model):
    project= models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="sections"
    )
    name= models.CharField(max_length=255)
    slug= models.SlugField(unique=True)
    position= models.IntegerField(default=0)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    class Meta:
        constraints= [
            models.UniqueConstraint(
                fields=["project", "slug"],
                name="unqiue_section_slug_per_project"
            )
        ]

class Page(models.Model):
    section= models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name="pages"
    )
    title= models.CharField(max_length=255)
    slug= models.SlugField(unique=True)
    description= models.TextField(blank=True)
    is_published=models.BooleanField(default=False)
    position= models.IntegerField(default=0)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    class Meta:
        constraints= [
            models.UniqueConstraint(
                fields=["section", "slug"],
                name="unqiue_page_slug_per_section"
            )
        ]