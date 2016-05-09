#! /usr/bin/python

#import requests.urlopen as urlopen
#from requests import urlopen
#from urllib.requests import urlopen
#import urllib3
import requests #pip install request==
from BeautifulSoup import BeautifulSoup #fixed error of 'obj module is not callable
from urlparse import urljoin 
from hashlib import sha256

import urllib
'''
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

html = urlopen("http://www.google.com/")
print(html.read())
'''

def grab_site_content(url):
    print "Yo Fetching website"
    
    r = requests.get(url)
    print r
    soup = BeautifulSoup(r.content)
    #links = [ a['href'] for a in soup.findAll('a',href=True)] 
    links = [ urljoin(url, a['href']) for a in soup.findAll('a',href=True) ]
    print links
    #^^NEEDS WORKS
    #Error when using find_all of 'Object not callable'
    for page in links:
        #Ignore the sitemap page
        if page == '/site/csc110winter2015/system/app/pages/sitemap/hierarchy':
            continue
        #page_req_test = urlopen(page)
        #print page_req_test
        
        with urllib.urlopen(page) as page_req:
            fingerprint = sha256()
            print fingerprint
        
    #for page in links:
        
    
        
    #Page encoding
    
    
    
        
    print links
    
    #print soup 

def save_site_summary(filename, summary):
    with open(filename, 'wt', encoding='utf-8') as f:
        for path, fingerprint in summary.items():
            f.write("{} {}\n".format(b64encode(fingerprint).decode(), path))


def main(url):
    grab_site_content(url)
    

#main(url='http://github.com/dsuarez4')
main(url='https://sites.google.com/site/csc110winter2015/home')

#EOF