from django.contrib import admin

from homepage.models import AboutPageModel, CardPageModel, ContactPageModel, HomePageModel, \
    PortfolioPageModel, SkillPageModel, BlogPageModel


@admin.register(HomePageModel)
class HomePageModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'mybio', 'mycvfile', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']

@admin.register(AboutPageModel)
class AboutPageModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']

@admin.register(CardPageModel)
class CardPageModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'numbers', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']

@admin.register(SkillPageModel)
class SkillPageModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'knowledge', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']

@admin.register(PortfolioPageModel)
class PortfolioPageModelAdmin(admin.ModelAdmin):
    list_display = ['githublink', 'youtubelink', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']

@admin.register(ContactPageModel)
class ContactPageModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'mylocation', 'mynumber', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'mylocation', 'mynumber']


@admin.register(BlogPageModel)
class BlogPageModel(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['created_at']
    search_fields = ['title']