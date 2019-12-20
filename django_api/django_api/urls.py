"""

The code in this file is coming from the django rest framework tutorial/documentation found at https:www.django-rest-framework.org/tutorial/quickstart

"""


from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from shoe_store import views


router = routers.DefaultRouter()
router.register(r'manufactorers', views.ManufactorerViewSet)
router.register(r'shoes', views.ShoeViewSet)
router.register(r'shoecolor', views.ShoeColorViewSet)
router.register(r'shoetype', views.ShoeTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]