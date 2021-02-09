import ScrapeSearchEngine
from ScrapeSearchEngine.SearchEngine import *

def twitter_search(name,pren):
    search = ("site:twitter.com \"{} {}\"".format(name,pren))
    try:
        googleText, googleLink = Google(search=search, userAgent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Safari/537.36")
        googleLinks = googleText[0:5]
        final_accounts = []
        for i in googleText:
            if "@" in i and name.lower() in i and pren.lower() in i:
                twitter_acc = ("@"+i.split('@')[1].split(')')[0])
                if twitter_acc in final_accounts:
                    pass
                else:
                    final_accounts.append(twitter_acc)
        if len(final_accounts) == 0:
            return None
        else:
            return final_accounts
    except:
        return None
