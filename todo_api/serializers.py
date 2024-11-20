from rest_framework import serializers
from .models import User, Task, Tag

class TagSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tags_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        write_only=True
    )
    class Meta:
        model = Tag
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True,)
    class Meta:
        model = Task
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'