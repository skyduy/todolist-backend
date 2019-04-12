from django.conf.urls import url, include
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url('^', include('todolist.urls')),
    url('^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^schema/$', schema_view),
]
