from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ContactInfo
from contact.v2.models import ContactInfoUpdate


class ContactInformationView(APIView):

    def get(self, request, *args, **kwargs):

        if request.version == 'v1':
            response = ContactInfo.objects.v1_data()
            return Response(response, status=status.HTTP_200_OK)
        elif request.version == 'v2':
            response = ContactInfoUpdate.objects.v2_data()
            return Response(response, status=status.HTTP_200_OK)


