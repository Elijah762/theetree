from django.urls import path
from .views import SignUpView, ProfileView, UpdateFileView
from . import views
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", views.ProfileView, name='profile'),
    path("signup/add-file", UpdateFileView.as_view(), name="update"),
]