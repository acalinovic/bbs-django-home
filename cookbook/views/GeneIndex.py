from django.views import generic

from cookbook.models import Gene


class GeneIndex(generic.ListView):
    model = Gene
