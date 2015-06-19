#! /usr/bin/python

#import requests.urlopen as urlopen
#from requests import urlopen
#from urllib.requests import urlopen
import urllib3
import requests #pip install request==
from BeautifulSoup import BeautifulSoup #fixed error of 'obj module is not callable
from urlparse import urljoin 

def grab_site_content(url):
    print "Yo Fetching website"
    
    r = requests.get(url)
    print r
    soup = BeautifulSoup(r.content)
    #links = [ a['href'] for a in soup.findAll('a',href=True)] 
    links = [ urljoin(url, a['href']) for a in soup.findAll('a',href=True)]
    #^^NEEDS WORKS
    #Error when using find_all of 'Object not callable'
    
    #for page in links:
        
    
        
    #Page encoding
    
    
    
        
    print links
    
    #print soup 
    


def main(url):
    grab_site_content(url)
    

main(url='http://github.com/dsuarez4')