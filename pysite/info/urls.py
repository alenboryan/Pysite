from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('about/', views.about, name="about"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.log_out),
    path("python_intro/", views.python_introduction, name ="python_intro"),
    path("error/", views.error, name="error"),
    path("python_syntax/", views.python_syntax, name = "python_syntax"), 
    path("create/", views.create, name = "create"),
    path("info_from_users/", views.add_info, name = "add_info"),
    path("django_info/", views.django_info, name = "django_info"),
    path("flask_info/", views.flask_info, name = "flask_info"),
    path("pandas_info/", views.pandas_info, name = "pandas_info"),
    path("numpy_info/", views.numpy_info, name = "numpy_info"),
]