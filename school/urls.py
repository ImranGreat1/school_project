"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),


    # Password Build In Views

    path(
        'password_reset/', auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset.html',
            email_template_name='registration/password_reset_email.html'
        ),
        name='password_reset'
    ),
    path(
        'password_reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'password_reset_confirm/<token>/<uidb64>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
