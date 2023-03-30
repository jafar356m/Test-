from django.urls import path,include
from .views import MyUserView
from rest_framework import routers
from softechapp.views import Taskviewset
from softechapp import views
from knox import views as knox_views
from .views import LoginAPI

router=routers.SimpleRouter()
router.register('posts',Taskviewset)
router.register('publish',views.completedTaskviewset)
router.register('unpublish',views.DueTaskviewset)


urlpatterns = [
    path('', MyUserView.as_view(), name='signup'),
    path('api_auth/',include('rest_framework.urls')),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('',include(router.urls))

    
]