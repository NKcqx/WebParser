from backend.core import cache, linker
from django.http import HttpResponse

def parseWeb (request):
    url = request.GET.get('url')
    result = cache.checkCache(url)
    return HttpResponse(linker.wrapInJSON(result))

