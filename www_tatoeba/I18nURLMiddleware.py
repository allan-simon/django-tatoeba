from django.utils import translation

class I18nURLMiddleware:
	def process_request(self, request):
		import re
		import settings
		check = re.match(r'/(\w+)\/.*', request.path)
		lang = settings.LANGUAGE_CODE
		if check is not None:
			t = check.group(1)
			if self.getSupportedLanguage().has_key(t):
				lang = self.getSupportedLanguage()[t]
			else:
				lang = settings.LANGUAGE_CODE
		request.session['django_language'] = lang

	def getSupportedLanguage(self):
		supportedLanguage = {
			'deu': 'de',
			'eng': 'en',
			'fre': 'fr'
		}
		return supportedLanguage


