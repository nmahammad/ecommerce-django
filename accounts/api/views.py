from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from accounts.api.serializers import RegistrationSerializers


@api_view(['POST',])
def registration_view(request):

 if request.method == 'POST':
  serializer = RegistrationSerializers(data=request.data)
  print(request.data)
  data = {}
  if serializer.is_valid():
   user = serializer.save()
   data['response'] = "successfully registered a new user"
   data['first_name'] = user.first_name
   data['last_name'] = user.last_name
   data['email'] = user.email
  else:
   data = serializer.errors
  return Response(data)
