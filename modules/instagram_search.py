import requests, bs4
from bs4      import BeautifulSoup

def ig_search(name,pren):
    url = "https://smihub.com/search?query={}+{}".format(pren,name)

    r = requests.get(url=url)
    page = r.content.decode()
    features = "html.parser"
    soup = BeautifulSoup(page,features)

    profiles = []

    profiless = soup.find_all('div',{'class':'content__text'})
    for i in profiless[0:10]:
        i = str(i)
        username = (i.split('</a><p>')[1].replace('</p></div>',''))
        at_username = (i.split('</a><p>')[0].split('Instagram\'s posts" class="profile-name-link" href="')[1].split('">')[1])
        profile_formated = ('{}\t| {}'.format(at_username,username))
        if name.lower() in profile_formated.lower() and name.lower() in profile_formated.lower():
            profiles.append(profile_formated)
    return profiles
