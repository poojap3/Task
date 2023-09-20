from django.urls import path, include
from .views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from . import views



app_name = 'Taskapp'


router = routers.DefaultRouter()

#to add the url
urlpatterns = [
    path('', include(router.urls)),


    path('task/', TaskAPIView.as_view(),name="TASK")]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
