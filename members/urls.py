from . import views
from django.urls import include, path
urlpatterns = [
    path('', views.index, name='index'),
    path('kelim', views.kelim, name='kelim'),
    path('kelimtwo', views.kelim, name='kelimtwo'),
    ]