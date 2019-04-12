from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from todolist import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'todolist', views.TaskViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url('', include(router.urls)),
]
