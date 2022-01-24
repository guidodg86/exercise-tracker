
from django.urls import path
from mainapp.views import CreateUserView

urlpatterns = [
    path('api/users', CreateUserView.as_view()),
]
