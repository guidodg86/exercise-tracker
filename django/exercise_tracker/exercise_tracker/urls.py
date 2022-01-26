
from django.urls import path
from mainapp.views import CreateUserView, CreateExerciseView, UserExerciseLogView

urlpatterns = [
    path('api/users', CreateUserView.as_view()),
    path('api/users/<str:id_user>/exercises', CreateExerciseView.as_view()),
    path('api/users/<str:id_user>/logs', UserExerciseLogView.as_view()),
]
