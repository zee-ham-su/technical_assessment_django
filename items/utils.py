from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        return Response({'detail': 'Item already exists.'},
                        status=status.HTTP_400_BAD_REQUEST)

    if response is not None:
        custom_response = {
            'errors': response.data,
            'status_code': response.status_code
        }
        response.data = custom_response

    return response
