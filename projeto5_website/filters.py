from dataclasses import field
from turtle import title
import django_filters
from .models import Article

class ArticleFilter(django_filters.filterset):
    dominancia = django_filters.CharFilter(lookup_expr='icontains')
    influencia = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model=Article
        fields=('dominancia', 'influencia')