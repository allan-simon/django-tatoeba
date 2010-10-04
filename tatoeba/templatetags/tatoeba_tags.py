from django import template
from django.core.urlresolvers import reverse
from django.utils import translation

register = template.Library()


@register.tag(name='tatoeba_url')
def do_tatoeba_url(parser, token):
    bits = token.split_contents()
    if len(bits) < 2:
        raise template.TemplateSyntaxError(
            "'%s' takes at least one argument (path to a view)" % bits[0]
        )

    viewname = bits[1]
    args = [translation.get_language()]

    if len(bits) > 2:
        for bit in iter(bits[2:]):
            args.append(bit)

    return TatoebaUrlNode(viewname, args)


class TatoebaUrlNode(template.Node):
    def __init__(self, viewname, args):
        self.viewname = viewname
        self.args = args

    def render(self, context):
        return reverse(self.viewname, args=self.args)
