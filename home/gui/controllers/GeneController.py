from cookbook.models import Gene


class GeneManager:
    model = Gene

    def get_gene_by_name(self, name):
        return self.model.objects.get(name=name)

    def get_gene_by_attr(self, **kwargs):
        return self.model.objects.get(**kwargs)
