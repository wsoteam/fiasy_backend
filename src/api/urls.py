from django.urls import path, include

from rest_framework import routers

from api.views.products import ProductViewset
from api.views.articles import ArticleViewset
from api.views.recipes import RecipeViewset

router = routers.DefaultRouter()
router.register('products', ProductViewset)
router.register('articles', ArticleViewset)
router.register('recipes', RecipeViewset)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/docs/', include('api.swagger_urls')),
    path('api/v1/auth/', include('rest_framework_social_oauth2.urls')),
]
