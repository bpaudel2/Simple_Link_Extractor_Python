import requests

def extract_link(page):
    start_link = page.find('href=')
    start_url = page.find('"',start_link)
    end_url = page.find('"',start_url+1)
    print (page[start_url+1:end_url])
    if start_link != -1:
        extract_link(page[end_url:])
def crawl(page):
    code = requests.get(page)
    plain = code.text
    extract_link(plain)
    
crawl('https://www.w3schools.com/')
crawl('https://www.udacity.com/')