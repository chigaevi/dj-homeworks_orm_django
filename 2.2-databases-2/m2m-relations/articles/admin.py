from django.contrib import admin
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope
from django.core.exceptions import ValidationError


class ScopeInLineFormset(BaseInlineFormSet):
    pass

class ScopeInline(admin.TabularInline):
    model = Scope



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    inlines = [ScopeInline,]
    formset = ScopeInLineFormset
    filter_vertical = ['tags']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass