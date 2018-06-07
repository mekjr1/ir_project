from django.shortcuts import render
import simplejson as json
from django.http import HttpResponse
from haystack.query import SearchQuerySet
from haystack.utils import Highlighter

#Search views
from django.views.generic import TemplateView

class SearchView(TemplateView):
    template_name = 'search_ir/search.html'
search_view = SearchView.as_view()




def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(model_auto=request.GET.get('q', ''))[:5]
    highlight = Highlighter(request.GET.get('q', ''), max_length=35)
    suggestions = [highlight.highlight(result.text) for result in sqs]
    print len(sqs)
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    the_data = json.dumps({
        'results': suggestions
    })
    return HttpResponse(the_data, content_type='application/json')