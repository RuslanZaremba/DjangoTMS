from django.contrib import admin
from django.urls import path, include
from my_blog.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('my_blog.urls')),
    path('accounts/login/', login, name='login'),
]
