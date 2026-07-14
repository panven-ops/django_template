from django.urls import path
from apps.core.views import health_check, readiness_check

urlpatterns = [path("health/", health_check, name = "health-check"),
               path("ready/", readiness_check, name = "readiness_check")]
