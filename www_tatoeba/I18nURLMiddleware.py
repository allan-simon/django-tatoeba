from django.utils import translation

class I18nURLMiddleware:
	def process_request(self, request):
		lang = self.getLanguageFromURL(request.path)
		translation.activate(lang)

	def getLanguageFromURL(self, url):
		import re
		import settings
		check = re.match(r'/(\w+)\/.*', url)
		lang = settings.LANGUAGE_CODE[0]
		if check is not None:
			t = check.group(1)
			if self.getSupportedLanguage().has_key(t):
				lang = self.getSupportedLanguage()[t]
			else:
				lang = settings.LANGUAGE_CODE[0]
		return lang

	def getSupportedLanguage(self):
		supportedLanguage = {
			'deu': 'de',
			'eng': 'en',
			'fre': 'fr'
		}
		return supportedLanguage


