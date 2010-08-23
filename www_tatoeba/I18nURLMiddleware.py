from django.utils import translation
from django.http import HttpResponseRedirect

class I18nURLMiddleware:
	def process_request(self, request):
		import re
		import settings
		check = re.match(r'/(?P<lang>\w+)/(?P<rest>.*)', request.path)
		lang = settings.LANGUAGE_CODE
		if check is not None:
			t = check.group('lang')
			if self.getSupportedLanguage().has_key(t):
				lang = self.getSupportedLanguage()[t]
			else:
				return HttpResponseRedirect('/eng/'+check.group('rest'))
		else:
			return HttpResponseRedirect('/eng/')
		request.session['django_language'] = lang

	def getSupportedLanguage(self):
		supportedLanguage = {
			'deu': 'de',
			'eng': 'en',
			'fre': 'fr'
		}
		return supportedLanguage


