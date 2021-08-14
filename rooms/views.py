from django.utils import timezone
from django.views.generic import ListView
from django.shortcuts import render
from django.http import Http404
from . import models, forms


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

    country = request.GET.get("country")

    if country:

        form = forms.SearchForm(request.GET)
        if form.is_valid():
            print(form.cleaned_data)

    else:
        form = forms.SearchForm()

    return render(
        request,
        "rooms/search.html",
        {"form": form},
    )
