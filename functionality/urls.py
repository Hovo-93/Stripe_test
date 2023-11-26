from django.conf.urls import include,url
from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

router = DefaultRouter()
router.register(r'item', views.ItemViewSet)




urlpatterns = [
    url(r'^', include(router.urls)),
    path('buy/<int:pk>', views.buy),

]