from django.urls import path
from .views import user_logout, user_login, user_register
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', user_login, name='login'),
    path("logout/", user_logout, name='logout'),
    path("register/", user_register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)