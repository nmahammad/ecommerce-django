from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from accounts.api.serializers import RegistrationSerializers

from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from accounts.api.serializers import UserSerializer


User = get_user_model()


class Register(APIView):
  # @swagger_auto_schema(query_serializer=RegistrationSerializers, request_body=RegistrationSerializers)
  def post(self, request, *args, **kwargs):
    """
      This endpoint for creat new user
    """
    serializer = RegistrationSerializers(data=request.data)
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

# @api_view(['POST',])
# def registration_view(request):
#  if request.method == 'POST':
#   serializer = RegistrationSerializers(data=request.data)
#   print(request.data)
#   data = {}
#   if serializer.is_valid():
#    user = serializer.save()
#    data['response'] = "successfully registered a new user"
#    data['first_name'] = user.first_name
#    data['last_name'] = user.last_name
#    data['email'] = user.email
#   else:
#    data = serializer.errors
#   return Response(data)
