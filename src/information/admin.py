from django import forms
from django.contrib import admin
from .models import Category, Article, AboutProject
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ArticleAdminForm(forms.ModelForm):
    text = forms.CharField(label='Текст статьи', widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):

    form = ArticleAdminForm


class AboutProjectAdminForm(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())

    class Meta:
        model = AboutProject
        fields = '__all__'


class AboutProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'for_str', )
    form = AboutProjectAdminForm


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(AboutProject, AboutProjectAdmin)
