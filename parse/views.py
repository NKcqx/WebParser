import json
from django.shortcuts import render
from mercury_parser import ParserAPI
from django.http import HttpResponse
from parse.models import *
# Create your views here.
def send_request (url):
    mercury = ParserAPI(api_key='cVwutZHUtwKpfsa1Dn2f93QDPdM6N5WKCCQIiVpb')
    return mercury.parse('http://www.cnblogs.com/leoo2sk/archive/2010/09/17/naive-bayesian-classifier.html')

def save_page(page):
    p = Page(
        title = page.title,
        content = page.content,
        date_published= page.date_published.strftime('%Y年%-m月%d日  %H:%m:%S'),
        lead_image_url= page.lead_image_url,
        dek= page.dek,
        url = page.url,
        domain = page.domain,
        excerpt =  page.excerpt,
        word_count = page.word_count,
        direction = page.direction,
        total_pages = page.total_pages,
        rendered_pages = page.rendered_pages,
        next_page_url = page.next_page_url
    )
    p.save()

def index (request):
    connect('test')
    page = Page(title="Title")
    page.num = 1
    page.save()
    page = Page.objects.get(title="Title")
    return render(request, 'index.html', {'title':'result.title', 'content': 'result.content'})
def parseWeb (request):
    url = request.GET.get('url')
    result = send_request(url)
    return HttpResponse(json.dumps({
                'title': result.title,
                'content': result.content,
                'date_published': result.date_published.strftime('%Y年%-m月%d日  %H:%m:%S'),
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

