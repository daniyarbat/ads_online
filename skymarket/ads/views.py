from rest_framework import pagination, viewsets, generics

from .models import Ad
from .serializers import AdSerializer, AdListSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AdListAPIView(generics.ListAPIView):
    serializer_class = AdListSerializer
    queryset = Ad.objects.all()

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    pass

