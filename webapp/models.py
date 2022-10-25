from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify



class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=False)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name 
    
    
class Project(models.Model):
    title = models.CharField(max_length=200, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_author', related_query_name='allproj')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_category', null=True)
    
    
    class Meta:
        ordering = ['-created_on']
        verbose_name = 'project'
        verbose_name_plural = 'projects'
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)
       
       
class MyDictionary(models.Model):
    words = models.CharField(max_length=200,  null=True, blank=True)
    type = models.CharField(max_length=200)
    meaning = models.TextField()  
    
    class Meta:
        ordering = ['words']
        verbose_name = 'My English Dictionary'
        verbose_name_plural = 'My English Dictionary'     
    
    def __str__(self):
        return self.words

    def save(self, *args, **kwargs):
        super(MyDictionary, self).save(*args, **kwargs)