from django.http import HttpResponseRedirect
from django.utils import translation
import re


class I18nUrlsMiddleware:
    def process_request(self, request):
        lang_code = self.get_language(request)

        check = re.match(r'/(?P<lang>\w+)(?P<rest>/?.*)', request.path)
        if check is not None:
            lang_url = check.group('lang')
            if lang_url == 'admin':
                pass
            elif lang_url != lang_code:
                return HttpResponseRedirect('/' + lang_code + check.group('rest'))
        else:
            return HttpResponseRedirect('/' + lang_code)

        request.session['django_language'] = lang_code
        return

    def get_language(self, request):
        oldLangCode = {
            'eng': 'en',
            'fre': 'fr'
        }

        from django.conf import settings
        supported = dict(settings.LANGUAGES)

        if hasattr(request, 'session'):
            lang_code = request.session.get('django_language', None)
            if lang_code in supported:
                return lang_code

        lang_code = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME)
        if lang_code in supported:
            return lang_code

        check = re.match(r'/(?P<lang>\w+)/.*', request.path)
        if check is not None:
            lang_code = check.group('lang')
            if lang_code in supported:
                return lang_code
            elif lang_code in oldLangCode:
                return oldLangCode[lang_code]

        return settings.LANGUAGE_CODE
