from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Project, Section, Page
from django.shortcuts import get_object_or_404
from .serializers import ProjectSerializer, SectionSerializer, PageSerializer, PublicProjectSerializer
# Create your views here.
class ProjectViewset(viewsets.ModelViewSet):
    serializer_class= ProjectSerializer
    permission_classes= [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(
            owner= self.request.user
        )
    def perform_create(self, serializer):
        serializer.save(
            owner= self.request.user
        )

class SectionViewset(viewsets.ModelViewSet):
    serializer_class= SectionSerializer
    permission_classes= [IsAuthenticated]

    def get_queryset(self):
        project = get_object_or_404(
                    Project,
                    id=self.kwargs["project_id"],
                    owner=self.request.user
                    )
        return Section.objects.filter(
            project= project,
            project__owner= self.request.user
        )
    def perform_create(self, serializer):
        project = get_object_or_404(
            Project,
            id=self.kwargs["project_id"],
            owner=self.request.user
        )
        serializer.save(
            project= project
        )
class PageViewset(viewsets.ModelViewSet):
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project = get_object_or_404(
            Project,
            id=self.kwargs["project_id"],
            owner=self.request.user
        )

        section = get_object_or_404(
            Section,
            id=self.kwargs["section_id"],
            project=project
        )

        return Page.objects.filter(section=section)

    def perform_create(self, serializer):
        project = get_object_or_404(
            Project,
            id=self.kwargs["project_id"],
            owner=self.request.user
        )

        section = get_object_or_404(
            Section,
            id=self.kwargs["section_id"],
            project=project
        )

        serializer.save(section=section)


class PublicProjectViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = PublicProjectSerializer
    permission_classes = [AllowAny]

    lookup_field = "slug"

    def get_queryset(self):
        return Project.objects.filter(
            is_visible=True
        )