from django.views.generic import CreateView, UpdateView, DetailView
from braces.views import LoginRequiredMixin
from .models import GlazeLookup


class GlazeLookupActionMixin(object):
    fields = ('glaze_name', 'slug', 'glaze_pieces', 'glaze_description', 'glaze_begin_date', 'glaze_end_date')

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(FlavorActionMixin, self).form_valid(form)


class GlazeLookupCreateView(LoginRequiredMixin, CreateView):
    model = GlazeLookup
    success_msg = "Glaze created!"



class GlazeLookupUpdateView(LoginRequiredMixin, UpdateView):
    model = GlazeLookup
    success_msg = "Glaze updated!"


class GlazeLookupDetailView(DetailView):
    model = GlazeLookup