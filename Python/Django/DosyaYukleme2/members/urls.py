from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('login/', views.login, name='login'),
    path('upload/', views.upload, name='upload'),
    path('search/<str:searchData>', views.search, name='search'),
    path('<str:searchData>', views.searchCategory, name='searchCategory'),
    path('exits/', views.exits, name='exits'),
    ]