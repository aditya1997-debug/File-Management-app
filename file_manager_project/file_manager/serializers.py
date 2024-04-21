from rest_framework import serializers
from .models import CustomUser, Company, File, Folder

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name']

class CustomUserSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'user_type', 'company']

class FileSerializer(serializers.ModelSerializer):
    shared_with = CustomUserSerializer(many=True, read_only=True)
    assigned_to = CustomUserSerializer(many=True, read_only=True)

    class Meta:
        model = File
        fields = ['name', 'file', 'owner', 'shared_with', 'assigned_to', 'parent_folder']

class CustomFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['file']

class FolderSerializer(serializers.ModelSerializer):
    files = CustomFileSerializer(many=True, read_only=True)
    owner = CustomUserSerializer(read_only=True)

    class Meta:
        model = Folder
        fields = ['id', 'name', 'owner', 'parent_folder', 'files']



