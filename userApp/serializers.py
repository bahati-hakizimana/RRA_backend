"""
This file contains serializers for the CustomUser model.
"""

from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'phone', 'role', 'created_at']
        read_only_fields = ['id', 'username', 'created_at']

from rest_framework import serializers
from .models import CustomUser

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'role']

    def validate_phone(self, value):
        if not value.startswith(('078', '079', '072', '073')) or len(value) != 10:
            raise serializers.ValidationError("Phone number must start with 078, 079, 072, or 073 and be 10 digits long.")
        if CustomUser.objects.filter(phone=value).exists():
            raise serializers.ValidationError("Phone number is already registered.")
        return value

    def validate_email(self, value):
        if not value.endswith('@gmail.com'):
            raise serializers.ValidationError("Email must end with @gmail.com.")
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already registered.")
        return value
    
    
    def validate_role(self, value):
        allowed_roles = ['unityuser', 'head of division', 'head of department']
        if value not in allowed_roles:
            raise serializers.ValidationError("Role must be one of: 'unit user', 'head of division', 'head of department'.")
        return value

    def create(self, validated_data):
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        username = f"{first_name}{last_name}{self.generate_random_string(5)}"
        password = self.generate_random_string(6)
        email = validated_data.get('email')
        phone = validated_data.get('phone')
        role = validated_data.get('role')
        

        user = CustomUser.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            phone=phone,
            role=role,
            password=password
        )

        # Send credentials via email
        self.send_credentials(email, username, password)

        return user

    def generate_random_string(self, length):
        import random
        import string
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def send_credentials(self, email, username, password):
        from django.core.mail import send_mail
        send_mail(
            'Welcome to RRA Report Management System',
            f'Hello,\n\nYou have been registered on RRA REPORT MANAGEMENT SYSTEM with the following details:\n\nUsername: {username}\nPassword: {password}\n\nYou can change these credentials after logging in.\n\nRegards!',
            'from@example.com',
            [email],
            fail_silently=False,
        )

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class PasswordResetSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    phone = serializers.CharField(required=False, allow_blank=True)

class UpdateUsernameSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False, allow_blank=True)
    phone = serializers.CharField(required=False, allow_blank=True)
    new_username = serializers.CharField()




class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
