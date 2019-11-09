from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/$', views.login, name='LoginView'),
    path('accounts/logout/$', views.logout, name='LogoutView', kwargs={'next_page': '/'}),
    path('', include('blog.urls')),
]
