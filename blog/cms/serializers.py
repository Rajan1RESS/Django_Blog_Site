from rest_framework import serializers
from .models import Author, Blog, Country
# from django.contrib.auth.models import User

MIN_LENGHT = 8

# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True,min_length=MIN_LENGHT,
#                                      error_messages = {
#                                         "min_length": f"Password must be longer than {MIN_LENGHT} characters."
#                                      }
#                                      )
    
#     password2 = serializers.CharField(write_only=True,min_length=MIN_LENGHT,
#                                     error_messages = {
#                                         "min_length": f"Password must be longer than {MIN_LENGHT} characters."
#                                      }
#                                     )
    
#     class Meta:
#         model = User
#         fields = "__all__"

#     def validate(self, data):
#         if data["password"] != data["password2"]:
#             raise serializers.ValidationError("Passwor does not match")
#         return data
    
#     def create(self, validated_data):
#         user = User.objects.create(
#             username = validated_data["username"],
#             email = validated_data["email"],
#             first_name = validated_data["first_name"],
#             last_name = validated_data["last_name"],
#         )

#         user.set_password(validated_data["password"])
#         user.save()

#         return user

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        exclude = []


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = []        

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = []        