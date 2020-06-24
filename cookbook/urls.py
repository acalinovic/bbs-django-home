from django.urls import path
from cookbook.views import *

urlpatterns = [
                  path('', BatchIndex.as_view(), name='batch_index'),
                  path('', GeneIndex.as_view(), name='gene_index'),
                  path('add/<int:gene_id>', batch_add, name='batch_add'),
                  path('del/<int:batch_id>', batch_del, name='batch_del'),
                  path('set/<int:batch_id>/<int:value>', batch_set, name='batch_set'),
                  path('setitem/<int:batch_item_id>/<str:value>', batch_set_item, name='batch_set_item'),
                  path('process', batch_process, name='batch_process'),
                  path('print', batch_report, name='batch_report'),
]
