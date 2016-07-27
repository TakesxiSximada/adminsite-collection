from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'pushes', views.PushViewSet)
