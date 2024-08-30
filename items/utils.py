from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        response = {
            'error': 'An unexpected error occurred.',
            'detail': str(exc)
        }
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    response.data['error'] = response.data.get('detail') or 'An unexpected error occurred.'
    response.data['status_code'] = response.status_code
    return response
