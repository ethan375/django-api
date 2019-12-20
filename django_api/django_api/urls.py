"""

The code in this file is coming from the django rest framework tutorial/documentation found at https:www.django-rest-framework.org/tutorial/quickstart

"""


from django.urls import include, path
from rest_framework import routers
from shoe_store import views


router = routers.DefaultRouter()
router.register(r'manufactorers', views.ManufactorerViewSet)
# router.register(r'shoes', views.)
# router.register(r'shoecolor', views.)
# router.register(r'shoetype', views)

urlpatterns = [
    path('', include(router.urls))
]