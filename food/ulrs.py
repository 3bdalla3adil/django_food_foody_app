from django.urls                import path,routers
from rest_framework.urlpatterns import format_suffix_patterns
from food.views                 import FoodDetail,FoodList
from . views                    import UserViewSet,GroupViewSet,index

app_name = 'food'


router = routers.DefaultRouter()

router.register('users' ,UserViewSet,basename='users')
router.register('groups',GroupViewSet,basename='groups')

urlpatterns = [
    path('users/' ,UserViewSet.as_view(), name='users'),
    path('groups/',GroupViewSet.as_view(), name='Groups'),
    path('food/' ,index),
    path('food/' ,FoodDetail),
    path('food/' ,FoodList),
]

urlpatterns = format_suffix_patterns(urlpatterns)