from .serializers import AboutSerializers, FAQSerializers
from . models import About, FAQ
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def about_api(request):
    about=About.objects.last()
    data=AboutSerializers(about).data
    return Response({'Success':True , 'data':data})




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def faq_api(request):
    faq=FAQ.objects.last()
    data=FAQSerializers(faq).data
    return Response({'Success':True , 'data':data})