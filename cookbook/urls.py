from django.urls import path

from cookbook.views.ReportIndex import *

urlpatterns = [
                  path('', ReportIndex.as_view(), name='report_index'),
                  path('add/<int:gene_id>/<int:report_id>', batch_add, name='batch_add'),
                  path('del/<int:batch_id>', batch_del, name='batch_del'),
                  path('delall', batch_del_all, name='batch_del_all'),
                  path('set/<int:batch_id>/<int:value>', batch_set, name='batch_set'),
                  path('setitem/<int:batch_item_id>/<str:value>', batch_set_item, name='batch_set_item'),
                  path('process', batch_process, name='batch_process'),
                  path('compute/<int:batch_id>', batch_render, name='batch_render'),
                  path('print/<int:report_id>', batch_report_print, name='batch_report_print'),
                  path('save/<int:report_id>', batch_report_save, name='batch_report_save'),
]
