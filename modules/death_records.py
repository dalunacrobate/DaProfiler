import ScrapeSearchEngine
from ScrapeSearchEngine.SearchEngine import *

def death_search(name,pren):
    search = ("site:dansnoscoeurs.fr \"{} {}\"".format(name,pren))
    try:
        googleText, googleLink = Google(search=search, userAgent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Safari/537.36")
        googleLinks = googleLink[0:5]
        final_links = []
        for i in googleLinks:
            if "https://www.dansnoscoeurs.fr/" in i and "/avis" in i:
                final_links.append(i)
        if len(final_links) == 0:
            return None
        else:
            return final_links
    except:
        return None
