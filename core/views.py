from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.conf import settings
from django.utils import timezone





@api_view(['GET'])
def health_check(request):
    
    return Response({
        'status': 'ok',
        'timestamp':timezone.now().isoformat(),
        'environment':(
            'development'
            if settings.DEBUG
            else 'production'
        )
    })