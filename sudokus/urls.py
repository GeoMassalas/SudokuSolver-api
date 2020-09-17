from rest_framework import routers
from .views import SudokuViewSet

router = routers.SimpleRouter()
router.register('', SudokuViewSet)
urlpatterns = router.urls

