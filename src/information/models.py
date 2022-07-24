from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название статьи')
    text = models.TextField(verbose_name='Текст статьи')
    date = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

    # def get_preview(self):
    #     if len(self.text) > 160:
    #         preview = self.text[:160]
    #     else:
    #         preview = self.text
    #     return f'{str(preview)}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class AboutProject(models.Model):
    title = models.CharField(max_length=255, verbose_name='Подзаголовок')
    for_str = models.CharField(max_length=255, verbose_name='Что вернёт __str__')
    text = models.TextField(verbose_name='Текст')
    email = models.CharField(max_length=100, verbose_name='E-mail')
    phone1 = models.CharField(max_length=14, verbose_name='Номер телефона')
    phone2 = models.CharField(max_length=14, null=True, blank=True, verbose_name='Номер телефона')

    def __str__(self):
        return self.for_str

    class Meta:
        verbose_name = 'О проекте'
        verbose_name_plural = 'О проекте'
