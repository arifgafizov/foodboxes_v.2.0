from app_items.views import ItemViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('items', ItemViewset, basename='item_viewset')
urlpatterns = router.urls
