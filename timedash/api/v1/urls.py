from rest_framework.routers import DefaultRouter
from .orders import OrderViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = router.urls