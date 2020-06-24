from . BatchIndex import BatchIndex, batch_process, batch_set_item, batch_report, batch_add, batch_del, batch_set
from . GeneIndex import GeneIndex
from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
