from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.


def HomeView(req):
    service = Services.objects.all()
    absets = AboutSect.objects.all()
    team = Team.objects.all()
    customers = Customers.objects.all()
    context = {
        "service": service,
        "abs": absets,
        "team": team,
        "csmr":customers,
    }
    return render(req, "index.html", context)


def SingleView(req, slug):
    service = get_object_or_404(Services, slug=slug)

    context = {"service": service}

    return render(req, "single.pg.html", context)



def AboutView(req):
    about = AboutUs.objects.all()

    context = {"about": about}

    return render(req, "about.html", context)

def ServiceView(req):
    services = Services.objects.all()

    context = {"services": services}

    return render(req, "services.html", context)


def WhyusView(req):
    why = AboutSect.objects.all()

    context = {"why": why}

    return render(req, "why.html", context)

def TeamView(req):
    team = Team.objects.all()

    context = {"team": team}

    return render(req, "team.html", context)