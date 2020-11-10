from django.urls import path
from .views import TodoList
from .views import TodoDetail
from .views import UserList
from .views import UserDetail
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("todos/", TodoList.as_view(), name="todo_list"),
    path('todo/<uuid:uuid>/', TodoDetail.as_view(), name="todo_details"),
    path('users/', UserList.as_view(), name="user_list"),
    path('user/<str:username>/', UserDetail.as_view(), name="user_details"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
