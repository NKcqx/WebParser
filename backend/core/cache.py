import logging
from . import linker
from parse.models import Page

''' ask for the Page from cache, if missed, the cache will ask it from remote server as a agent'''
def checkCache(url):
    # return URI in cache (ask for it and save to cache if isn't in cache
    logging('check cache', url)

    if(missCache(url)):
        logging.info('cache missed, file: ', url)
        result = addCache(url)
    else:
        # cache hit, check whether overdue or not
        if(isCacheOverdue(url)):
            logging.info('update cache', url)
            updateCache(url)
        result = Page.objects(url = url)
    return result

''' test wether missed cache or not'''
def missCache(url):
    objs = Page.objects(url = url)
    return len(objs) == 0

def updateCache(url): # just for updates via url, others can use ORM directly
    result = linker.send_request(url)
    obj = Page.objects.get(url = url)
    for k, v in result:
        obj[k] = v
    # TODO: updateLocalFile(url)
    return obj # i.e. pk

def addCache(url):
    result = linker.send_request(url)
    obj = Page()
    for k, v in result:
        obj[k] = v
    # TODO: updateLocalFile(url)
    obj.save()
    return obj

def deleteCache(id):
    Page.objects.delete(pk=id)

def updateLocalFile(url):
    file = open(url, 'w')


def isCacheOverdue(url):
    return False # TODO