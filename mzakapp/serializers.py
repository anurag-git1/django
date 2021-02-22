from rest_framework import serializers
from .models import User,CustomerReportRecord
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User                
        fields = '__all__'
        
    # field level validation
    # def validate_email(self, value):
    
    #     if '@gmail.com' not in value:
    #         raise serializers.ValidationError("A valid email must be entered")
    #     return value
    
    # object level validation
    # def validate(self,data):
    #     email = data.get('email')
    #     print("email",email)

# class UserSerializer(serializers.Serializer):
#     email = serializers.EmailField(
#         max_length=100,
#         style={'placeholder': 'Email', 'autofocus': True}
#     )
#     password = serializers.CharField(
#         max_length=100,
#         style={'input_type': 'password', 'placeholder': 'Password'}
#     )
#     remember_me = serializers.BooleanField()

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.contact = validated_data.get('contact',instance.contact)
        instance.save()
        return instance

class CustomerReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerReportRecord
        fields = '__all__'