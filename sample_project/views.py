from django.views.generic import TemplateView
from .models import BornIn, DiedIn

class BirthDeathListView(TemplateView):
    template_name = "sample_project/birth_death_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["born_relations"] = BornIn.objects.order_by("date")
        context["died_relations"] = DiedIn.objects.order_by("date")
        return context