from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ClientSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at',
                  'created_by', 'updated_at']


class ProjectSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    users = UserSerializer(many=True, read_only=True)
    client_id = serializers.IntegerField(write_only=True)
    users_id = serializers.ListField(
        write_only=True, child=serializers.IntegerField())

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'client_id',
                  'users', 'users_id', 'created_at', 'created_by']

    def create(self, validated_data):
        client_id = validated_data.pop('client_id')
        users_id = validated_data.pop('users_id')
        project = Project.objects.create(**validated_data)
        project.client = Client.objects.get(id=client_id)
        project.users.set(User.objects.filter(id__in=users_id))
        project.save()
        return project
