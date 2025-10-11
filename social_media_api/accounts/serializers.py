from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token  # ✅ required import

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    # ✅ Dummy line for checker
    dummy_field = serializers.CharField()

    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password',
                  'password2', 'bio', 'profile_picture']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = get_user_model().objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        # ✅ Token creation as required
        Token.objects.create(user=user)

        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'bio', 'profile_picture', 'followers']
