from django.urls import path, include
from blog import views as v
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/register/', v.register, name='register'),
    path('', include('blog.urls')),
]