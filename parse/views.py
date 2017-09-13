import json
from django.shortcuts import render
from mercury_parser import ParserAPI
from django.http import HttpResponse
# Create your views here.
def parse (url):
    mercury = ParserAPI(api_key='cVwutZHUtwKpfsa1Dn2f93QDPdM6N5WKCCQIiVpb')
    return mercury.parse('http://www.cnblogs.com/leoo2sk/archive/2010/09/17/naive-bayesian-classifier.html')

def index (request):
    return render(request, 'index.html', {'title':' result.title', 'content': 'result.content'})
def parseWeb (request):
    url = request.GET.get('url')
    result = parse(url)
    print('result', json.dumps({
                'title': result.title,
                'date_published': result.date_published.strftime('%Y-%-m-%d %H:%m:%S'),
                'lead_image_url': result.lead_image_url,
                'def': result.dek,
                'url': result.url,
                'domain': result.domain,
                'excerpt': result.excerpt,
                'word_count': result.word_count,
                'direction': result.direction,
                'total_pages': result.total_pages,
                'rendered_pages': result.rendered_pages,
                'next_page_url': result.next_page_url
            }))
    return HttpResponse(json.dumps({
                'title': result.title,
                'content': result.content,
                'date_published': result.date_published.strftime('%Y-%-m-%d %H:%m:%S'),
                'lead_image_url': result.lead_image_url,
                'def': result.dek,
                'url': result.url,
                'domain': result.domain,
                'excerpt': result.excerpt,
                'word_count': result.word_count,
                'direction': result.direction,
                'total_pages': result.total_pages,
                'rendered_pages': result.rendered_pages,
                'next_page_url': result.next_page_url
            }))
