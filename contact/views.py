from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContactSerializer
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings
import json
# Create your views here.

@api_view(['GET'])
def contactList(request):
    ''' get data from contact form '''
    contact = Contact.objects.all()
    serielizer = ContactSerializer(contact, many=True)
    return Response(serielizer.data)

@api_view(['POST'])
def CreateContact(request):
    ''' post data to contact form and send email'''
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        send_mail(
            'Sending Email',
            json.dumps(request.data),
            settings.EMAIL_HOST_USER,
            ['aleksandr.sekker@gmail.com',],
            fail_silently=False,
)
    return Response(serializer.data)
