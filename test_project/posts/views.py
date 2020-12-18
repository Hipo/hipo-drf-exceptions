from django.utils.translation import ugettext as _
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from posts.exceptions import InvalidTitleError
from posts.serializers import PostSerializer


class CreatePostView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        if request.data['title'] == 'View Invalid Title':
            raise InvalidTitleError(detail={'title': _('Invalid title at the view level.')})
        return super(CreatePostView, self).post(request, *args, **kwargs)
