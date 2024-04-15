from django.urls import path,include

from rest_framework import routers
from rest_framework.authtoken import views

from .views import DepartmanMVS,PersonMVS,logout

router = routers.DefaultRouter()
router.register('departman',DepartmanMVS)
router.register('person',PersonMVS)


urlpatterns = [
    path('',include(router.urls)),
    path('login/', views.obtain_auth_token),
    path('logout/',logout),
   
]
    



