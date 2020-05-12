from rest_framework.exceptions import ValidationError

from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "is_staff",
        )

    def validate(self, data):
        validated_data = super().validate(data)
        if validated_data["first_name"] == "invalid_serializer_first_name":
            raise ValidationError({"first_name": "Invalid entry at the serializer level."})
        return validated_data
