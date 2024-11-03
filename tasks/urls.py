from django.urls import path,include
from rest_framework.routers import DefaultRouter

from tasks.views import TaskViewSet,ListTodoView

router = DefaultRouter()
router.register(r'',TaskViewSet,basename='tasks')

urlpatterns = [
    path('tasks/',include(router.urls)),
    path('todolist/',ListTodoView.as_view()),
]
