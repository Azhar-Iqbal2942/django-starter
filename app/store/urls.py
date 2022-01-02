from rest_framework.routers import DefaultRouter

# Custom Imports
from store.views.customer_views import CustomerViewSet
from store.views.product_views import ProductViewSet

router = DefaultRouter()
router.register('customers',CustomerViewSet)
router.register('products',ProductViewSet)

urlpatterns = router.urls