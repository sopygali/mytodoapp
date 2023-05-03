from rest_framework.serializers import ModelSerializer
from base.models import Task, User, Mark

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class UserSerialaizer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MarkSerialaizer(ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'