from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, PatientViewSet, DoctorViewSet, MappingViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('patients', PatientViewSet, basename='patients')
router.register('doctors', DoctorViewSet, basename='doctors')
router.register('mappings', MappingViewSet, basename='mappings')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
