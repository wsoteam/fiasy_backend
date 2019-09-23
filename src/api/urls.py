from django.urls import path, include

from rest_framework import routers

from api.views.products import ProductViewset
from api.views.articles import ArticleViewset
from api.views.recipes import RecipeViewset
from api.views.user_profile import UserViewset, UserProfileViewset

from rest_framework_simplejwt import views as jwt_views


router = routers.DefaultRouter()
router.register('products', ProductViewset)
router.register('articles', ArticleViewset)
router.register('recipes', RecipeViewset)
router.register('users', UserViewset)
router.register('user_profiles', UserProfileViewset)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/docs/', include('api.swagger_urls')),
    path('api/auth/token/', jwt_views.TokenObtainPairView.as_view()),
    path('api/auth/token/refresh/', jwt_views.TokenRefreshView.as_view()),
]
