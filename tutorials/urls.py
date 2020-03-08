from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'tutorials', views.TutorialViewSet)

urlpatterns = [
    path('', include(router.urls))
]
