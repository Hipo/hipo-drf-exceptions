from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^api/users/', include(('users.urls', 'users'), namespace='users')),
]
