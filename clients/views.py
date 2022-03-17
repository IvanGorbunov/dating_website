from clients.models import User
from clients.serializers import UserDetailSerializer
from clients.utils import MultiSerializerViewSet


class UserViewSet(MultiSerializerViewSet):
    queryset = User.objects.all()
    serializers = {
        'create': UserDetailSerializer,
    }

    def create(self, request, *args, **kwargs):
        """
        Создание клиента
        """
        return super().create(request, *args, **kwargs)