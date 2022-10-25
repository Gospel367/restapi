from django.urls import path
from webapp import views 
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('users/', views.UserView.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('category/', views.CategoryView.as_view(), name='category_list' ),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category_detail' ),
    path('projects/', views.ProjectView.as_view(), name='project_list'),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='project_detail' ),
    path('dictionary/create/', views.MyDictionaryCreate.as_view(), name='create-dictionary'),
    path('dictionary/', views.MyDictionaryView.as_view(), name='dictionary_list'),
    path('dictionary/<int:pk>/', views.MyDictionaryDetail.as_view(), name='dictionary_detail' ),
    path('dictionary/<int:pk>/update/', views.MyDictionaryUpdate.as_view(), name='dictionary_update' ),
    path('dictionary/<int:pk>/delete/', views.MyDictionaryDelete.as_view(), name='dictionary_delete' ),
    path('dictionary-search/', views.dictionaryview, name='dictionary'),
])

