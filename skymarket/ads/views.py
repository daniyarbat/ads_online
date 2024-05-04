from rest_framework import pagination, viewsets, generics

from .models import Ad, Comment
from .serializers import AdSerializer, AdListSerializer, CommentListSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    pagination_class = AdPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AdListAPIView(generics.ListAPIView):
    serializer_class = AdListSerializer
    queryset = Ad.objects.all()
    pagination_class = AdPagination

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentListSerializer
    queryset = Comment.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.action == "create":
            return CommentSerializer
        return CommentListSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, ad_id=self.kwargs['ad_pk'])

    def get_queryset(self):
        return Comment.objects.filter(ad_id=self.kwargs['ad_pk'])
