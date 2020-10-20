
from django.views import generic
from cookbook.models import Report


class ReportView(generic.DetailView):

    def get_queryset(self):
        return Report.objects.create()
