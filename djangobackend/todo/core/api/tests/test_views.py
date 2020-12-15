import json

from django.urls import reverse
from django.contrib.auth import get_user_model

from todo.core.base.models import Todo
from todo.core.api.serializers import TodoSerializer

from rest_framework import status
from rest_framework.test import APITestCase


User = get_user_model()

class TestTokenObtainPairView(APITestCase):
    def setUp(self):
        self.url = reverse('todoapi:token_obtain_pair')
        self.username = "user"
        self.password = "password"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_authentication_without_password(self):
        """
        Vérifier qu'un utilisateur ne peut pas se connecter sans entrer un mdp
        """
        response = self.client.post(self.url, {"username": self.username}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_authentication_incorrect_credentials(self):
        """
        Vérifier qu'un utilisateur avec des identifiants non corrects n'arrive pas à se connecter
        """
        response = self.client.post(self.url, {'username':'incorrect', 'password':'incorrect'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authentication_incorrect_password(self):
        """
        Vérifier qu'un utilisateur avec un mot de passe non correct n'arrive pas à se connecter
        """
        response = self.client.post(self.url, {"username": self.username, "password": "incorrect"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authentication_correct_credentials(self):
        """
        Vérifier qu'un utilisateur avec un id/mdp corrects arrive à se connecter
        """
        response = self.client.post(self.url, {"username": self.username, "password": self.password}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)


class TestTodoList(APITestCase):
    def setUp(self):
        self.url = reverse('todoapi:todo_list')
        self.username = "user"
        self.password = "password"
        self.user = User.objects.create_user(self.username, self.password)
        self.client.force_authenticate(user=self.user)

    def test_create_todo_unauthenticated(self):
        """
        Vérifier qu'un utilisateur non authentifié ne peut pas créer un todo
        """
        self.client.force_authenticate(user=None)
        response = self.client.post(self.url, {"value": "Rendre le travail !"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_todo_authenticated(self):
        """
        Vérifier qu'un utilisateur authentifié peut créer un todo
        """
        response = self.client.post(self.url, {"value": "Rendre le travail !"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_todos_unauthenticated(self):
        """
        Vérifier qu'un utilisateur non-authentifié n'a pas accès à une liste de todos
        """
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_todos_authenticated(self):
        """
        Vérifier qu'un utilisateur authentifié a accès à sa liste de todos
        """
        Todo.objects.create(owner=self.user, value="Rendre le travail !")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(json.loads(response.content)) == Todo.objects.count())


class TestTodoDetail(APITestCase):
    def setUp(self):
        self.username = "user"
        self.password = "password"
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.client.force_authenticate(user=self.user)
        self.todo = Todo.objects.create(owner=self.user, value="Rendre le travail !")
        self.url = reverse('todoapi:todo_details', kwargs={"uuid": self.todo.uuid})

    def test_get_todo_unauthenticated(self):
        """
        Vérifie qu'un utilisateur non-authentifié ne peut pas lire un todo
        """
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_todo_authenticated(self):
        """
        Vérifier qu'un utilisateur peut récupérer son todo
        """
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

        todo_serializer_data = TodoSerializer(instance=self.todo).data
        response_data = json.loads(response.content)
        self.assertEqual(todo_serializer_data, response_data)


    def test_update_todo_not_owner(self):
        """
        Vérifier qu'un utilisateur ne peut pas mettre à jour un todo d'un autre utilisateur
        """
        new_user = User.objects.create_user(username="newuser", password="newpassword")
        self.client.force_authenticate(user=new_user)

        # PUT
        response = self.client.put(self.url, {"value", "lol"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # PATCH
        response = self.client.patch(self.url, {"value", "lol"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_todo_owner(self):
        """
        Vérifier qu'un utilisateur peut mettre à jour son todo
        """
        response = self.client.put(self.url, {"value": "Dormir !"})
        response_data = json.loads(response.content)
        todo = Todo.objects.get(uuid=self.todo.uuid)
        self.assertEqual(response_data.get("value"), todo.value)

    def test_update_check_todo_owner(self):
        """
        Vérifier qu'un utilisateur peut mettre à jour son todo à checked
        """
        response = self.client.patch(self.url, {"checked": True})
        response_data = json.loads(response.content)
        todo = Todo.objects.get(uuid=self.todo.uuid)
        self.assertEqual(response_data.get("checked"), todo.checked)

    def test_delete_todo_not_owner(self):
        """
        Vérifier qu'un utilisateur ne peut pas supprimer le todo d'un autre utilisateur
        """
        new_user = User.objects.create_user(username="newuser", password="newpassword")
        self.client.force_authenticate(user=new_user)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_todo_owner(self):
        """
        Vérifier que le propiétaire d'un todo peut le supprimer
        """
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
