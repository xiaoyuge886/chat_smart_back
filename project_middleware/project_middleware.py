"""
@ Author:   gy
@ Date :    2022/8/10
"""
import json
import traceback
from django.http import HttpResponse, JsonResponse, HttpResponseServerError
from django.utils.deprecation import MiddlewareMixin
from rest_framework.exceptions import APIException


class DealResponseMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        res_data = dict()
        # response = self.get_response(request)
        if hasattr(response, 'data'):
            data = response.data
            del response.data
            res_data['data'] = data
            res_data['code'] = 0
            res_data['message'] = 'success'
            response.data = res_data
            response._is_rendered = False
            response.render()
        return response

    def process_exception(self, request, exception):
        traceback.print_exc()
        exception_class = exception.__class__
        if exception_class == APIException:
            return HttpResponse(json.dumps({'err_msg': 'bad param'}), status=400)
        raise exception

