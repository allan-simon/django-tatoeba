from django.conf import settings
from django.utils import translation
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect

class I18nUrlsMiddleware:
	def process_request(self, request):
		import re
		check = re.match(r'/(?P<language>\w+)(?P<rest>/?.*)', request.path)
		if check is not None:
			language = check.group('language')
			supported = dict(settings.LANGUAGES)
			
			if supported.has_key(language):
				translation.activate(language)
			elif language == 'admin':
				pass
			elif self.getOldLanguageCode().has_key(language):
				url = request.path.replace(language, self.getOldLanguageCode()[language], 1)
				return HttpResponsePermanentRedirect(url)
			else:
				url = '/'+translation.get_language()+'/'+language+check.group('rest')
				return HttpResponseRedirect(url)
		else:
			return HttpResponseRedirect('/'+translation.get_language())


#    def process_response(self, request, response):
#        if (reponse.has_key('location')):
#            response['location'] = '/fr/' + response['location']
#        return response

	def getOldLanguageCode(self):
		lang = {
			'deu': 'de',
			'eng': 'en',
			'fre': 'fr'
		}
		return lang
