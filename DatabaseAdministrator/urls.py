"""
URL configuration for DatabaseAdministrator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
# from .user.views import profile, login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    # path('login/', LoginView.as_view(), name='login'),
    # path('login/', login, name='login'),
    # path('profile/', profile, name='profile'),
    # path('logout/', logout, name='logout'),
    # path('', views.display_charts, name='index'),
    # path('filters', views.filter_options,name='filter_options'),
    # path('annual/<int:year>/sales', views.get_annual_sales, name='annual_chart'),
]
