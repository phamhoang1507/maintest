from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['title','body','author','image']

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['id','username','email','first_name','last_name','password']
        extra_kwargs={
            'password':{'write_only':'true'}
        }

    def create(self, validated_data):
        user=User(**validated_data)
        user.set_password( validated_data['password'])
        user.save()

        return user

