from rest_framework import mixins,permissions,viewsets
# Create your views here.
from blog.serializers import BlogSerializer
from blog.models import Blog
class BlogViewset(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    serializer_class=BlogSerializer
    queryset=Blog.objects.all()
