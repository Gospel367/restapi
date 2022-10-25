from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, MyDictionary, Project
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.HyperlinkedModelSerializer):
    project_author = serializers.HyperlinkedIdentityField(many=True, view_name='project_detail', read_only=True)
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).update(instance, validated_data)
    
    class Meta:
        model = User
        fields = ['pk',  'username', 'email', 'password', 'is_superuser',  'project_author']
        
        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    post_category = serializers.HyperlinkedRelatedField(many=True, view_name='project_detail', read_only=True)
    
    class Meta:
        model = Category
        fields = ['pk', 'name', 'slug',  'post_category']

        
class ProjectSerializer(serializers.ModelSerializer):
    post_author = serializers.ReadOnlyField(source='author.username')
    post_category = serializers.ReadOnlyField(source='category.name')
    
    class Meta:
        model = Project
        fields = ['pk', 'title', 'description', 'created_on', 'author', 'category',  'post_author', 'post_category']
        
        
class MyDictionarySerializer(serializers.ModelSerializer):

    class Meta:
        model = MyDictionary
        fields = ['pk', 'words', 'type', 'meaning']
        
        '''def create(self, validated_data):
            # learn this....
            return super(UserSerializer, self).create(validated_data)'''
            
        

