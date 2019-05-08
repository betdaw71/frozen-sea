from django.contrib import admin
from film_article.models import Article, Genre,Category,Star_article
# Register your models here.
admin.site.register(Article)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Star_article)
