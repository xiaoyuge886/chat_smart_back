"""smart_chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path("admin/", admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from smart_chat.smart_router import get_router
from apps.smart_token.views import SmartTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title=' API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(get_router().urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', schema_view, name="docs"),
    path('api-token/', views.obtain_auth_token),
]

# 获取token
urlpatterns += [
    # path('api-jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-jwt/token/', SmartTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-jwt/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# from apps.chats.views import Chat
# urlpatterns += [
#     path('chat/', Chat.as_view()),
#
# ]

# urlpatterns += [
#     path('api/chat/', Chat.as_view({}))
# ]
