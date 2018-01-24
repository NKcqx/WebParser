import json
import logging

from mercury_parser import ParserAPI

def send_request(url):
    mercury = ParserAPI(api_key='cVwutZHUtwKpfsa1Dn2f93QDPdM6N5WKCCQIiVpb')
    return mercury.parse(url)

def wrapInJSON(result): # change result from dict to json
    return json.dumps({
                'title': result.title,
                'content': result.content,
                'date_published': result.date_published.strftime('%Y年%-m月%d日  %H:%m:%S'),
                'lead_image_url': result.lead_image_url,
                'dek': result.dek,
                'url': result.url,
                'domain': result.domain,
                'excerpt': result.excerpt,
                'word_count': result.word_count,
                'direction': result.direction,
                'total_pages': result.total_pages,
                'rendered_pages': result.rendered_pages,
                'next_page_url': result.next_page_url
            })
