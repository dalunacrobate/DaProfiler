import requests, bs4
from bs4      import BeautifulSoup

def ig_search(name,pren):
    headers = {
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
'referrer': 'https://google.com',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'utf-8',
'Accept-Language': 'en-US,en;q=0.9',
'Pragma': 'no-cache'
}
    r = requests.get(url='https://instajust.com/search/{} {}'.format(name,pren),headers=headers)
    page = r.content
    features = "html.parser"
    soup = BeautifulSoup(page, features)
    profiles = soup.find_all('div',{'class':'trending_inst--inst'})
    new_profiles = []
    for i in profiles:
        i = i.text
        if pren.lower() in i.lower() and name.lower() in i.lower():
            profile = (i.replace('\n','').replace('@',' | @'))
            new_profiles.append(profile)
    return new_profiles
