from django.shortcuts import render

# Create your views here.

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import permissions

from apps.chats.chat_api import main_chat

from apps.chats.serializer import RecordSerializer

from apps.chats.models import Record

from rest_framework.response import Response
from utils.smart_throttling import UserRateThrottle
from rest_framework.throttling import AnonRateThrottle, ScopedRateThrottle

import logging
api_logger = logging.getLogger('log')


class Chat(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    # authentication_classes = []
    serializer_class = RecordSerializer
    queryset = Record.objects.all()
    throttle_scope = 'chats'
    throttle_classes = [UserRateThrottle, ScopedRateThrottle, AnonRateThrottle]

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = RecordSerializer(data=request.data)
        data = request.data
        res = main_chat(data.get("content"))
        api_logger.info(res)
        return Response(res)
