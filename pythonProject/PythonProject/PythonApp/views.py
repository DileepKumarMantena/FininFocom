import json
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *



class RegistrationApi(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            return Response({'message': 'Successful',
                             'Result': RegistrationSerializer(user).data,
                             'HasError': False,
                             'status': 200})
        except Exception as e:
            return Response({'message': 'Fail',
                             'Result': [],
                             'HasError': True,
                             'status': 400})
