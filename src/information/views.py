from django.shortcuts import render
from .models import Category, Article, AboutProject


def home(request):
    category = Category.objects.all()
    context = {
        'categorises': category
    }
    return render(request, 'information/home2.html', context)


def article_list(request, category_id):
    category = Category.objects.get(pk=category_id)
    articles = Article.objects.filter(category=category_id)
    category_title = category.title
    category_description = category.category_description
    context = {
        'articles': articles,
        'category': category_title,
        'description': category_description,
    }
    return render(request, 'information/article_list.html', context)


def article_detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    category_id = article.category.id
    context = {
        'article': article,
        'category_id': category_id
    }
    return render(request, 'information/article_detail.html', context)


def about(request):
    about_project = AboutProject.objects.all()
    context = {
        'about_project': about_project
    }
    return render(request, 'information/about_project.html', context)
