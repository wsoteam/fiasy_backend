from django.urls import path, include

from rest_framework import routers

from api.views.products import (
    ProductViewset,
    EnProductViewset,
    DeProductViewset,
    PtProductViewset,
    EsProductViewset,
    GetProductViewset,
    EnGetProductViewset,
    DeGetProductViewset,
    PtGetProductViewset,
    EsGetProductViewset
)

# from api.views.user_profile import AddFavProductView, DeleteFavProductView
from api.views.articles import ArticleViewset, ArticleSeriesViewset
from api.views.recipes import RecipeViewset
from api.views.user_profile import UserViewset, UserProfileViewset
from api.views.sendsay import SendsaySetMemberView
from api.views.feedbacks import FeedbackView, FeedbackTypeView
from api.views.diet_plans import DietPlanViewset
from api.views.meals import MealsViewset
from api.views.water import WaterViewset
from api.views.body_measurements import BodyMeasurementViewset
from api.views.intermittent_fasting import FastingViewset

from rest_framework_simplejwt import views as jwt_views


en_router = routers.DefaultRouter()
en_router.register('products', EnProductViewset)
en_router.register('search', EnGetProductViewset, base_name='search')

de_router = routers.DefaultRouter()
de_router.register('products', DeProductViewset)
de_router.register('search', DeGetProductViewset, base_name='search')

es_router = routers.DefaultRouter()
es_router.register('products', PtProductViewset)
es_router.register('search', EsGetProductViewset, base_name='search')

pt_router = routers.DefaultRouter()
pt_router.register('products', PtProductViewset)
pt_router.register('search', PtGetProductViewset, base_name='search')

router = routers.DefaultRouter()
router.register('search', GetProductViewset, base_name='search')
router.register('products', ProductViewset, base_name='producs')
router.register('articles', ArticleViewset)
router.register('articles/series', ArticleSeriesViewset)
router.register('recipes', RecipeViewset)
router.register('diet_plans', DietPlanViewset)
router.register('users', UserViewset)
router.register('user_profiles', UserProfileViewset)
router.register('meals', MealsViewset)
router.register('water', WaterViewset)
router.register('body_measurements', BodyMeasurementViewset)
router.register('intermittent_fasting', FastingViewset)

urlpatterns = [
    path('api/v1/en/', include(en_router.urls)),
    path('api/v1/de/', include(de_router.urls)),
    path('api/v1/es/', include(es_router.urls)),
    path('api/v1/pt/', include(pt_router.urls)),
    path('api/v1/', include(router.urls)),
    path('api/v1/feedbacks/feedback_types', FeedbackTypeView.as_view()),
    path('api/v1/feedbacks/set/', FeedbackView.as_view()),
    path('api/v1/sendsay/set/', SendsaySetMemberView.as_view()),
    # path('api/v1/add_favorite_product/', AddFavProductView.as_view()),
    # path('api/v1/delete_favorite_product/', DeleteFavProductView.as_view()),
    path('api/docs/', include('api.swagger_urls')),
    path('api/auth/token/', jwt_views.TokenObtainPairView.as_view()),
    path('api/auth/token/refresh/', jwt_views.TokenRefreshView.as_view()),
]
