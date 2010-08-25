from django.conf import settings
from django.utils import translation
from django.http import HttpResponseRedirect

class I18nUrlsMiddleware:
	def process_view(self, request, view_func, view_args, view_kwargs):
		language = view_kwargs.get('language', None)
		supported = dict(settings.LANGUAGES)
		if language:
			if supported.has_key(language):
				translation.activate(language)
			#elif old pages
			else:
				url = request.path.replace(language, translation.get_language(), 1)
				return HttpResponseRedirect(url)
		else:
			return HttpResponseRedirect('/'+translation.get_language())
