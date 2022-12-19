from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r"api/", include("app.urls")),
    path(r'users/', include('users.urls')),
]
