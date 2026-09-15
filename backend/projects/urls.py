from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProjectViewset, SectionViewset, PageViewset, PublicProjectViewset


router = DefaultRouter()

router.register(
    r"projects",
    ProjectViewset,
    basename="project"
)

router.register(
    r"project-docs",
    PublicProjectViewset,
    basename="public-project"
)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "projects/<int:project_id>/sections/",
        SectionViewset.as_view({
            "get": "list",
            "post": "create",
        }),
        name="sections"
    ),

    path(
        "projects/<int:project_id>/sections/<int:pk>/",
        SectionViewset.as_view({
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy",
        }),
        name="sections"
    ),

    path(
    "projects/<int:project_id>/sections/<int:section_id>/pages/",
    PageViewset.as_view({
        "get": "list",
        "post": "create",
    }),
    ),
    path(
    "projects/<int:project_id>/sections/<int:section_id>/pages/<int:pk>/",
    PageViewset.as_view({
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }),
    ),
]