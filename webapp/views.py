
from ast import Return
from dataclasses import dataclass
from django.template import RequestContext
from django.views.generic import ListView, TemplateView
from django.http import Http404, response,request
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from pyparsing import Word
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, MultiPartRenderer
from rest_framework import generics, permissions, status
from restapi.settings import DATABASES
from webapp.forms import DictForm
from webapp.models import Category, MyDictionary, Project
from webapp.permissions import IsOwnerOrReadyOnly
from .serializers import CategorySerializer, MyDictionarySerializer, UserSerializer, ProjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from webapp import serializers
from rest_framework.reverse import reverse
from PyDictionary import PyDictionary

dictionary =PyDictionary()
'''#Using class_based views and overriding
class UserView(APIView):
    renderer_classes = [TemplateRenderer]
    
    def get(self, request, format=None):
        all_users = User.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return Response(serializer.data, template_name='project)
    
    def post(self, request, format=None):
        serializer =UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class UserDetail(APIView):
    
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        single_user = self.get_object(pk)
        serializer = UserSerializer(single_user)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        single_user = self.get_object(pk)
        serializer =UserSerializer(single_user, data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        single_user = self.get_object(pk)
        single_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''
    
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user_list', request=request, format=format),
        'projects': reverse('project_list', request=request, format=format),
        'categories': reverse('category_list', request=request, format=format),
        'dictionary': reverse('dictionary_list', request=request, format=format)
    })

#using generic class based views
class UserView(generics.ListCreateAPIView):
    queryset =User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    serializers
    
    
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('first_name')
    serializer_class= UserSerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]
    
    
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class =  CategorySerializer
    permission_classes = [permissions.IsAdminUser]
    
    
class ProjectView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    
class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadyOnly]
    
    
class MyDictionaryView(generics.ListAPIView):
    queryset = MyDictionary.objects.all()
    serializer_class = MyDictionarySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
class MyDictionaryDetail(generics.RetrieveAPIView):
    queryset = MyDictionary.objects.all()
    serializer_class = MyDictionarySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
class MyDictionaryUpdate(generics.RetrieveUpdateAPIView):
    queryset = MyDictionary.objects.all()
    serializer_class = MyDictionarySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class MyDictionaryDelete(generics.RetrieveDestroyAPIView):
    queryset = MyDictionary.objects.all()
    serializer_class = MyDictionarySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
class MyDictionaryCreate(generics.ListCreateAPIView):
    queryset = MyDictionary.objects.all()
    serializer_class = MyDictionarySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    '''def perform_create(self, serializer):
        #learn this
        return super().perform_create(serializer)'''
    
    
    

def dictionaryview(request):
    if request.method =='POST':
        
        search_word = request.POST.get("searchword")
        if search_word =='':
            error = 'Error! Please input a value to get result'
            return render(request, 'output.html', {'error': error})
        elif not '':
            search_word_cleaned =search_word.lower()
            search_word_cleaned = (search_word[0].capitalize() + search_word[1:])
            output = MyDictionary.objects.filter(words=(str(search_word_cleaned)))
            synonym = dictionary.synonym(search_word)
            antonym = dictionary.antonym(search_word)
            if output.exists():
                return render(request, 'output.html', {'output': output, 'antonym': antonym, 'synonym': synonym})
            else:
                #return redirect('dictionary_list')
                meaning = dictionary.meaning(search_word)
                if meaning != None:
                    addition = MyDictionary.objects.create(words=search_word_cleaned, type = type, meaning=meaning)
                    addition.save()
                
                return render(request, 'output.html', {'meaning': meaning,  'antonym': antonym, 'synonym': synonym, 'search_word_cleaned': search_word_cleaned})
    else:
        return render(request, 'dictionary.html', {})
    
