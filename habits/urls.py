"""
URLs для приложения habits.
Используется DRF DefaultRouter для HabitViewSet.
"""

from rest_framework.routers import DefaultRouter
from .views import HabitViewSet

router = DefaultRouter()
router.register(r"habits", HabitViewSet, basename="habit")

urlpatterns = list(router.urls)
