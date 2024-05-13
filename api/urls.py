from .views import TopicViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'topics', TopicViewSet)

urlpatterns = router.urls