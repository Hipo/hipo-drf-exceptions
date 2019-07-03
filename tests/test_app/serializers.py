from rest_framework import fields, serializers

from tests.test_app.models import Item


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = (
            "name",
        )
