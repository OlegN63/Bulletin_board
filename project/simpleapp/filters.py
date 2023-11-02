from django_filters import FilterSet, CharFilter
from .models import Post
from django import forms

class PostFilter(FilterSet):
    header = CharFilter(lookup_expr='icontains', label='По заголовку')
    author = CharFilter(lookup_expr='icontains', label='По имени автора')

    class Meta:
        model = Post
        fields = ['header', 'author']