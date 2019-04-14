from todolist.models import Task
from todolist.serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework import filters


class TaskOrdering(filters.OrderingFilter):
    allowed_custom_filters = {'-created', '-priority', 'expired'}

    def filter_queryset(self, request, queryset, view):
        params = self.get_ordering(request, queryset, view);
        if params is None:
            return queryset
        ordering = [i for i in params if i in self.allowed_custom_filters]
        if ordering:
            return queryset.order_by(*ordering)
        return queryset


class TaskViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_fields = ['completed']
    filter_backends = (filters.DjangoFilterBackend, TaskOrdering,)
