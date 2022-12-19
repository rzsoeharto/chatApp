from urllib.parse import parse_qs

from channels.db import database_sync_to_async
from api.models import UserData
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, TokenError

# User = UserData


# @database_sync_to_async
# def get_user(user_id):
#     try:
#         return User.objects.get(id=user_id)
#     except User.DoesNotExist:
#         return Response({"Message": "Unauthorized Please Log in"}, status=status.HTTP_401_UNAUTHORIZED)


# class WebSocketJWTAuthMiddleware:
#     def __init__(self, app):
#         self.app = app

#     async def __call__(self, scope, received, send):
#         parsed_query_string = parse_qs(scope["query_string"])
#         token = parsed_query_string.get(b"token")[0].decode("utf-8")

#         try:
#             access_token = AccessToken(token)
#             scope["user"] = await get_user(access_token["user_id"])
#         except TokenError:
#             print("Something went wrong")

#         return await self.app(scope, received, send)
