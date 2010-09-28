from django import template
from django.core.urlresolvers import reverse
from django.utils import translation

register = template.Library()

#register.tag(name="tatoeba_url")
def do_tatoeba_url(parser, token):
	try:
		args = token.split_contents()
	except ValueError:
		raise template.TemplateSyntaxError, "tatoeba_url syntax error"
	return TatoebaUrlNode(args)

class TatoebaUrlNode(template.Node):
	def __init__(self, args):
		self.args = args
	def render(self, context):
		a = [translation.get_language()]
		for i in range(2, len(self.args)):
			a.append(self.args[i])

		return reverse(self.args[1], args=a)

register.tag('tatoeba_url', do_tatoeba_url)

