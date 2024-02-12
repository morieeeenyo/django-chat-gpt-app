from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"threads", views.ThreadViewSet)

urlpatterns = [
    path("messages/", views.MessageView.as_view()),
]

urlpatterns += router.urls
