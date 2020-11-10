from rest_framework import serializers
from django.contrib.auth import get_user_model
from . import models


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk','first_name', 'middle_name', 'last_name'
                ,'email','date_of_birth', 'mobile_number','gender',
                'address'
                  )

    # def create(self, validated_data):
    #     validated_data['password'] = make_password(validated_data.get('password'))
    #     return super(UserSerializer, self).create(validated_data)


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    class Meta:
        model = models.Product
        fields = '__all__'        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'