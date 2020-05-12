from django.urls import path

from users import views

urlpatterns = [
    path(r'register/', views.RegistrationView.as_view(), name='register'),
]
