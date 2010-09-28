from django import template

register = template.Library()

#register.tag(name="tatoeba_url")
def do_tatoeba_url(parser, token):
	try:
		kwargs = token.split_contents()
	except ValueError:
		raise template.TemplateSyntaxError, "tatoeba_url syntax error"
	return TateobaUrlNode(kwards)

class TatoebaUrlNode(template.Node):
	def __init__(self, kwards):
		self.kwards = kwards
	def render(self, context):
		return "toto"

register.tag('tatoeba_url', do_tatoeba_url)

