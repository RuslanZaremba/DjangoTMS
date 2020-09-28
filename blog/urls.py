from django.contrib import admin
from django.urls import path, include
from my_blog.views import login

urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('my_blog.urls')),
]
