from django.utils import translation
from django.http import HttpResponseRedirect

class I18nURLMiddleware:
	def process_request(self, request):
		import re
		import settings
		check = re.match(r'/(?P<lang>\w+)/(?P<rest>.*)', request.path)
		i18nLang = settings.LANGUAGE_CODE
		if check is not None:
			t = check.group('lang')
			if t in self.getLang():
				i18nLang = self.getI18n()[self.getLang().index(t)]
			else:
				t = request.COOKIES.get('django_language', i18nLang)
				lang = self.getLang()[self.getI18n().index(t)]

				return HttpResponseRedirect('/'+lang+'/'+check.group('rest'))
		else:
			t = request.COOKIES.get('django_language', i18nLang)
			lang = self.getLang()[self.getI18n().index(t)]
			return HttpResponseRedirect('/'+lang+'/')
		request.session['django_language'] = i18nLang

	def process_response(self, request, response):
		response.set_cookie('django_language', request.session['django_language'])
		return response

	def getI18n(self):
		i18n = [
			'de',
			'en',
			'fr'
		]
		return i18n
	
	def getLang(self):
		lang = [
			'deu',
			'eng',
			'fre'
		]
		return lang


