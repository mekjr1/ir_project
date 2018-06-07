{% load poll_extras %}

from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(needs_autoescape=True)
def initial_letter_filter(text, autoescape=True):
    first, other = text[0], text[1:]
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = '<strong>%s</strong>%s' % (esc(first), esc(other))
    return mark_safe(result)


def process_res():
	query=["rapists", "jakarta"]
	c=0
	sent = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)(\s|[A-Z].*)',text)
	sent_res=[]
	for s in sent:
	    if len(sent_res)==len(query):
	                break
	    for it in query:
	        if it in s.lower():
	            rep="<strong>"+it+"</strong>"
	            h=s.lower().replace(it, rep)
	            sent_res.append(h)
	            break
	    
	print sent_res        

	bim ={key: text.lower().count(key) for key in query}

	return bim, sent_res