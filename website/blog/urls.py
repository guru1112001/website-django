
from django.urls import path
from . import views
from .models import blogs

from django.urls import path, include
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class blogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = blogs
        fields = ['tittle']

# ViewSets define the view behavior.
class blogViewSet(viewsets.ModelViewSet):
    queryset = blogs.objects.all()
    serializer_class = blogSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'blogs', blogViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('blog', views.bloglistview.as_view()),
]