import requests, bs4
from bs4 import BeautifulSoup

"""
La source utilisée ne retourne pas à 100% les profils trouvés, malheuresement c'est la seule que j'ai trouvé pour rechercher des profils sur twitter;
Pull Request si tu as une suggestion, celle-ci serra appréciée.
"""

def twitter_search(name,pren):
    try:
        url = "https://tweet.lambda.dance/search?f=users&q={}+{}".format(pren,name)

        r = requests.get(url)
        page = r.content
        features = "html.parser"
        soup = BeautifulSoup(page, features)

        full_name = soup.find_all('div',{'class':'tweet-name-row'})
        username  = soup.find_all('a',{'class':'username'})

        final_accounts = []

        for i in range(len(full_name)):
            usernamee = username[i].text
            fullname  = full_name[i].text
            final_accounts.append(
                '{}\t|{}'.format(usernamee,fullname)
            )
        if len(final_accounts) == 0:
            return None
        else:
            return final_accounts
    except:
        return None
