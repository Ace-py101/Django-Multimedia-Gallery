from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "media/<int:pk>/",
        views.media_detail,
        name="media_detail"
    ),

]