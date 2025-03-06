"""
URL configuration for historical_helper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from events.views import *

urlpatterns = [
    path('', index, name='home'),
    path('admin/', admin.site.urls),
    path('events_war/', events_list_war),
    path('events_company/', events_list_company),
    path('event_war/<int:id>/', event_war),
    path('event_company/<int:id>/', event_company),
    path('chat/', ai_chat, name='ai_chat'),
    path('accounts/register/', register, name='register'),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
]
