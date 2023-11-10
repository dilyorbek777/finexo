from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeView, name="home"),
    path("about/", AboutView, name="about"),
    path("service/", ServiceView, name="service"),
    path("why/", WhyusView, name="why"),
    path("team/", TeamView, name="team"),
    path("services/<slug:slug>/", SingleView, name="single"),
]
