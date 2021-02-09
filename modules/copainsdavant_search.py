import requests, bs4, colorama
from bs4 import BeautifulSoup

def copains_davant(name,pren):
    r = requests.get('http://copainsdavant.linternaute.com/s/?ty=1&prenom={}&nom={}'.format(pren,name))
    pagephone = r.content
    featuresphone = "html.parser"
    soup = BeautifulSoup(pagephone,featuresphone)

    try:
        url = str(soup.find_all("h3"))
        url = (url.split('href="')[1].split('</a>')[0].split('">')[0])

        r = requests.get("http://copainsdavant.linternaute.com{}".format(url))
        pagephone = r.content
        featuresphone = "html.parser"
        soup = BeautifulSoup(pagephone,featuresphone)

        url_full = "http://copainsdavant.linternaute.com{}".format(url)
        try:
            localisation = str(soup.find('span',{'class':'locality'}).text)
            naissance = str(soup.find('abbr',{'class':'bday'}).text)
            name_full = str(soup.find('figure',{'class':'jLogo'}).text.strip())
            if name.lower() in name_full.lower() and pren.lower() in name_full.lower():
                text = {'full_name':name_full,'born':naissance,'localisation':localisation,'url_full':url_full}
                return text
            else:
                return None
        except AttributeError:
            return None
    except IndexError:
        return None
