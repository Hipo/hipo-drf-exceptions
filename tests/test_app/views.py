from rest_framework.generics import CreateAPIView

from tests.test_app.serializers import ItemSerializer


class CreateItemView(CreateAPIView):
    permission_classes = ()
    serializer_class = ItemSerializer
