import datetime
from haystack import indexes
from search_ir.models import News



class NewsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    model_auto = indexes.EdgeNgramField(model_attr='text')

    

    def get_model(self):
        return News

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""

        return self.get_model().objects.all()