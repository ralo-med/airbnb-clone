from django.utils import timezone
from django.views.generic import ListView
from django.shortcuts import render
from django_countries import countries
from django.http import Http404
from . import models


# Create your views here.
class HomeView(ListView):

    """HomeView definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404()


"""
class RoomDetail(DetailView):

    model = models.Room
"""


def search(request):
    print(request.GET)
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(
        request.GET.get(
            "room_type",
        )
    )
    room_types = models.RoomType.objects.all()

    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
    }

    choices = {
        "countries": countries,
        "room_types": room_types,
    }

    return render(
        request,
        "rooms/search.html",
        {**form, **choices},
    )
