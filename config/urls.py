from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/api/hello/")),
    path("api/", include("api.urls")),
]
