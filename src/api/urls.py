from django.urls import path, include

from rest_framework import routers

from api.views.products import ProductViewset
from api.views.articles import ArticleViewset

router = routers.DefaultRouter()
router.register('products', ProductViewset)
router.register('articles', ArticleViewset)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
