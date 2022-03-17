import json

from django.urls import reverse_lazy

from clients.models import User
from clients.utils import WithLoginTestCase


class TestViews(WithLoginTestCase):

    def test_create_client(self):
        data = {
            "username": "user32233",
            "password": "password",
            "first_name": "user2322",
            "last_name": "user2322",
            "email": "email22@email.com",
        }

        url = reverse_lazy('clients:create_client')
        response = self.client.post(url, data=json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 201)

        user = User.objects.filter(username=data['username']).first()   # type: User
        self.assertEqual(response.data['username'], user.username, response.data)
        self.assertEqual(response.data['first_name'], user.first_name, response.data)
        self.assertEqual(response.data['last_name'], user.last_name, response.data)
        self.assertEqual(response.data['email'], user.email, response.data)