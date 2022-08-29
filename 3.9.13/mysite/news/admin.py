from django.contrib import admin

from .models import News, Category #Импорт модели

class NewsAdmin(admin.ModelAdmin): #Настройка отображения в АДМ
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published') #Отображение по выбранным полям
    list_display_links = ('id', 'title') #Выбор поля в качестве ссылки на модель
    search_fields = ('title', 'content') #Добавить поиск по выбранному полю
    list_editable = ('is_published',) #Редактировать из списка
    list_filter = ('is_published', 'category')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(News, NewsAdmin) #Регистрация модели
admin.site.register(Category, CategoryAdmin)