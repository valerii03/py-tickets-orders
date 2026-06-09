from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    MovieSessionViewSet,
    OrderViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register(r"movies", MovieViewSet)
router.register(r"movie_sessions", MovieSessionViewSet)
router.register(r"orders", OrderViewSet, basename="orders")

urlpatterns = router.urls
