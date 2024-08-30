from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from django.http import HttpResponse
from rest_framework.exceptions import NotFound
from django.core.paginator import EmptyPage
from django.db import IntegrityError


def api_root(request):
    return HttpResponse("Welcome to My Items API!")


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

    def paginate_queryset(self, queryset):
        page_number = self.request.query_params.get('page')
        if page_number is None:
            page_number = 1
        try:
            return super().paginate_queryset(queryset)
        except EmptyPage:
            raise NotFound("Page not found.")

    def get_object(self):
        try:
            return super().get_object()
        except Item.DoesNotExist:
            raise NotFound(detail="Item not found",
                           code=status.HTTP_404_NOT_FOUND)
