from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True)
    password2 = serializers.CharField(write_only=True)  # confirm password

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

        # ✅ uses get_user_model().objects.create_user
        user = get_user_model().objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'bio', 'profile_picture', 'followers']
