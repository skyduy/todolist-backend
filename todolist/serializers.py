from rest_framework import serializers
from todolist.models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('url', 'id', 'created', 'completed', 'context',
                  'priority', 'expired')
