from urllib import response
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden
from django.conf import settings
import logging
import requests


class LogginMiddleware(MiddlewareMixin):

    def process_request(self,request):


        logging.info("Request Method : "+str(request.META["REQUEST_METHOD"]))
        logging.info("URL Requested : "+str(request.path))
        logging.info("Request Body Contents : "+str(request.body))
        logging.info("Content Length : "+str(request.META["CONTENT_LENGTH"]))
        logging.info("Client IP Address : "+str(request.META["REMOTE_ADDR"]))
        logging.info("Host Name of CLient : "+str(request.META["REMOTE_HOST"]))
        logging.info("Host Name of the Server : "+str(request.META["SERVER_NAME"]))
        logging.info("Port of the Server : "+str(request.META["SERVER_PORT"]))       
        return None
    
    # def process_response(self,response,request):
    #     # Response = requests.get('http://127.0.0.1:8000/')
    #     # logging.info("Response code : " + str(Response.status_code))
    #     # logging.info("Response content : " + str(dir(response)))
    #     pass



class BlockIPMiddleware(MiddlewareMixin):
    BLACKLIST = [
        '10.10.81.198',
    ]

    def process_view(self, request, *args, **kwargs):
     
        if request.META['REMOTE_ADDR'] in self.BLACKLIST:
            return HttpResponseForbidden()


# rsgplyanccjavxjk