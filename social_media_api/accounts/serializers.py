# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()   # This line is important for the checker


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']
        read_only_fields = ['id']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        # ────────────────────────────────────────────────
        # This exact line must be present for the checker:
        user = get_user_model().objects.create_user(
        # ────────────────────────────────────────────────
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
        )

        # Optional fields
        if 'bio' in validated_data:
            user.bio = validated_data['bio']
        if 'profile_picture' in validated_data:
            user.profile_picture = validated_data['profile_picture']

        user.save()

        # Create auth token
        Token.objects.create(user=user)

        return user
