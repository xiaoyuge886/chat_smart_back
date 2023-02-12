"""
@ Author:   gy
@ Date :    2022/8/8
"""

from rest_framework import routers
from apps.chats.views import Chat

router = routers.DefaultRouter()
# router.register(r'chat', Chat, basename="api-chat")
router.register(r'api/v1/chat', Chat, basename='api-v1-chat')


def get_router():
    return router
