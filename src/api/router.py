from rest_framework import routers
from api.views.comments import CommentsViewSet
from api.views.locations import LocationViewSet

from api.views.tourism_spot import TourismSpotViewSet
from api.views.attractions import AttractionsViewSet
from api.views.reviews import ReviewViewSet


router = routers.DefaultRouter()
router.register(r'tourismspots', TourismSpotViewSet)
router.register(r'attractions', AttractionsViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'comments', CommentsViewSet)
router.register(r'reviews', ReviewViewSet)
