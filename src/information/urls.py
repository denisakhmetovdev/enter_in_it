from django.urls import path
from .views import home, article_list, article_detail, about


urlpatterns = [
    path('article_list/<int:category_id>/', article_list, name='article_list'),
    path('article_detail/<int:article_id>/', article_detail, name='article'),
    path('about_project/', about, name='about'),
    path('', home, name='home')
]
