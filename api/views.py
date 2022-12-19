from django.shortcuts import render

# Create your views here.
from .serializers import UserSerializer
from .models import Listing
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated


# @api_view(["POST"])
# def registerUser(req):
#     email = req.data.get("email")
#     username = req.data.get("username")
#     password = req.data.get("password")
#     if User.objects.filter(email=email).exists():
#         return Response({"Message": "A user with that email already exists"}, status=status.HTTP_302_FOUND)
#     if User.objects.filter(username=username).exists():
#         return Response({"Message": "That username is taken"}, status=status.HTTP_302_FOUND)
#     else:
#         user = User.objects.create_user(email=email, password=password, username=username)
#         user.save()
#         return Response({"Message": "passed"}, status=status.HTTP_201_CREATED)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["email"] = user.email
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["POST"])
def logUserIn(req):
    username = req.data.get("username")
    password = req.data.get("password")
    user = authenticate(req, username=username, password=password)
    if user is not None:
        login(req, user)
        return Response({"Message": "success"}, status=status.HTTP_200_OK)
    else:
        return Response({"Message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createListing(req):
    # get everything from request
    userID = req.data.get("userID")
    email = req.data.get("email")
    productName = req.data.get("productName")
    clotheType = req.data.get("clotheType")
    price = req.data.get("price")
    size = req.data.get("size")
    condition = req.data.get("condition")
    style = req.data.get("style")
    colour = req.data.get("colour")

    #
    Listing.objects.create(
        productName=productName,
        clotheType=clotheType,
        price=price,
        size=size,
        condition=condition,
        style=style,
        colour=colour,
    )

    return Response({"Message": "OK"}, status=status.HTTP_200_OK)


# view for registering users
@api_view(["POST"])
def registerView(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"Register": "success"}, status=status.HTTP_200_OK)


class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        user = self.request.user
        try:
            isAuthenticated = user.is_authenticated

            if isAuthenticated:
                return Response({"isAuthenticated": "success"}, status=status.HTTP_200_OK)
            else:
                return Response({"isAuthenticated": "error"}, status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(
                {"error": "Something went wrong when checking authentication status"},
                status=status.HTTP_417_EXPECTATION_FAILED,
            )
