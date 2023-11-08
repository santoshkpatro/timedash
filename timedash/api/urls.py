from django.urls import path, include

urlpatterns = [
    path("v1/", include("timedash.api.v1.urls")),
]
