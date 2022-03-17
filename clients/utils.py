
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet

from django.test import override_settings
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from clients.models import User

from django.utils.timezone import now as tz_now


def generate_uniq_code():
    return str(tz_now().timestamp()).replace('.', '')


class MultiSerializerViewSet(ModelViewSet):
    filtersets = {
        'default': None,
    }
    serializers = {
        'default': Serializer,
    }

    @property
    def filterset_class(self):
        return self.filtersets.get(self.action) or self.filtersets.get('default')

    @property
    def serializer_class(self):
        return self.serializers.get(self.action) or self.serializers.get('default', Serializer)

    def get_response(self, data=None):
        return Response(data)

    def get_valid_data(self, many=False):
        serializer = self.get_serializer(data=self.request.data, many=many)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data


@override_settings(SQL_DEBUG=False)
class TestCaseBase(APITestCase):
    """
    Базовый (без авторизации)
    """
    CONTENT_TYPE_JSON = 'application/json'

    def check_status(self, response, status):
        self.assertEqual(response.status_code, status, response.data)

    def generate_uniq_code(self):
        return generate_uniq_code()


class WithLoginTestCase(TestCaseBase):
    """
    С авторизацией
    """
    @classmethod
    def setUpClass(cls):
        user, is_create = User.objects.get_or_create(username='admin')
        if is_create:
            user.set_password('admin')
            user.save()
        cls.user = user
        cls.token, _ = Token.objects.get_or_create(user=user)
        super().setUpClass()

    def setUp(self) -> None:
        self.auth_user(self.user)
        super().setUp()

    def auth_user(self, user):
        """
        Авторизация
        """
        token, _ = Token.objects.get_or_create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

