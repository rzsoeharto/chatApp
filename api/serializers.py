from rest_framework import serializers
from .models import Listing, UserData


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ["id", "email", "name", "password"]

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data["email"], name=validated_data["name"])
        user.set_password(validated_data["password"])
        user.save()
        return user


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = (Listing,)
        fields = "__all__"
