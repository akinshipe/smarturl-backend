
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import UrlSerializer, UrlSerializer1
from django.contrib.auth.models import User
from django.db import transaction
from .models import Url
from rest_framework import status
import math
import string
import random
import time
from datetime import date

###########################################################################################################################################
## this views(called controller by M V C engineers) are in no way ready for production, multiple validation and case scenarios handling have not been implemented


# please replace the base url with the domain you are deploying the frontend app to, dont forget to add the domain to the corrs origin white list in settings.py
#  make sure the baseurl ends with a backslash, also take into consideration if you are deploying on http or https

BASERL = 'http://localhost:3000/'




# this view is responsible for the shortening of the url, it uses a very non-scalable algorithm to shorten the url. if this was a production app, i will pre-generate shortened url 
# to several tables and use a mapping funcrion to assign the shortened urls to new incoming request (sort of like the way hash table data structure works). if collision exist i will use linear probbing to solve it 
# this view is far from production ready as input validation has not been done

class ShortenUrl(APIView):
   
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        time.sleep(1)

        serializer = UrlSerializer1(data=request.data)
        serializer.is_valid(raise_exception=True)

        long_url = serializer.data['long_url']

        query_set = Url.objects.filter(long_url=long_url)

        if query_set.exists():
            url_object = query_set.first()

            serializer = UrlSerializer(url_object)

            return Response(serializer.data, status = status.HTTP_202_ACCEPTED )

        else:

            while True:

                count = round(math.sqrt(len(long_url)))
                short_url = BASERL + "".join(random.choices(
                    string.ascii_letters + string.digits, k=count))

                query_set = Url.objects.filter(short_url=short_url)

                if not query_set.exists():
                    break
            
            data = {'long_url': long_url, 'short_url': short_url}
            if request.user.is_authenticated:
                data['url_owner'] = request.user.id
            serializer = UrlSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response(serializer.data, status = status.HTTP_201_CREATED)



## this views handle the user registration and is no way ready for production as it has little to no input data validation

class RegisterNewUser(APIView):

    def post(self, request):
        time.sleep(1)

        queryset = User.objects.filter(username=request.data['username'])

        if queryset.exists():
            return Response('Username already exist, if you are the owner please login', status = status.HTTP_403_FORBIDDEN)

        user = User.objects.create_user(
            request.data['username'],
            email=request.data['email'],
            password=request.data['password'],

        )

        with transaction.atomic():

            user.save()
            query, created = Token.objects.get_or_create(user=user)

       

        return Response('Account created succesfully, please login', status=status.HTTP_201_CREATED)



## this views handle the user login and is no way ready for production as it has little to no input data validation

class Login(APIView):

    def post(self, request, format=None):
        time.sleep(1)

        login_data = request.data

        current_user = User.objects.filter(
            username=login_data['username'])

        if current_user.exists():

            current_user = current_user.first()

            password_verification = current_user.check_password(
                login_data['password'])

            if password_verification == True:
                user_token = Token.objects.filter(
                    user_id=current_user.id).first()

                token, created = Token.objects.get_or_create(user=current_user)

                data = dict(username=current_user.username, user_id = current_user.id,
                            email=current_user.email, token=token.key)

                return Response(data, status = status.HTTP_202_ACCEPTED)

            else:
                return Response({"non_field_errors": ["Unable to log in with provided credentials."]}, status = status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"non_field_errors": ["Unable to log in with provided credentials."]}, status = status.HTTP_400_BAD_REQUEST)


# this views handle the list of urls for the logged in user requesting it
class GetUserUrls(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        time.sleep(1)

        query = Url.objects.filter(url_owner = request.user.id).order_by("-created_time")


        serializer = UrlSerializer(query, many = True)
      

        return Response(serializer.data, status.HTTP_200_OK)



# the get destination views is quite simple, it takes a shortened url and send back the long url. little or no input data validation has been done, there by it is not production ready
class GetDestinationUrl(APIView):
   
    def post(self, request):
        time.sleep(5)

        queryset = Url.objects.filter(short_url = request.data['short_url'])

        if not queryset.exists():
            return Response("We could not recognise this URL", status = status.HTTP_400_BAD_REQUEST )

        query = queryset.first()

        query.visits = query.visits + 1

        query.last_visit_time = date.today()

        query.save()

        serializer = UrlSerializer(query)
      
        return Response(serializer.data['long_url'], status = status.HTTP_200_OK)

     