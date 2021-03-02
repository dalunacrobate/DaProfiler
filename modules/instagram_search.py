import requests, bs4
from bs4      import BeautifulSoup

def getInstagramEmailFromBio(username):
    url = "https://smihub.com/v/{}".format(username)
    r = requests.get(url)
    page = r.content.decode()
    features = "html.parser"
    soup = BeautifulSoup(page,features)
    try:
        bio = soup.find('div',{'class':'user__info-desc'}).text

        words = bio.split(' ')

        emails = [
            '@icloud.com',
            '@gmail.com',
            '@gmx.fr',
            '@yahoo.fr',
            '@yahoo.com',
            '@outlook.com'
            '@outlook.fr',
            '@hotmail.fr',
            '@hotmail.com',
            '@live.fr',
            '@live.com',
            '@sfr.fr',
            '@orange.fr',
            '@free.fr',
            '@aol.com',
            '@wanadoo.fr',
            '@neuf.fr',
            '@laposte.net',
            '@yandex.ru',
            '@club-internet.fr',
            '@msn.com',
            '@influencelife.fr',
            '@shaunaevents.com',
            '@we-events.fr',
            '@nabillapro.com',
            '@facebook.com'
        ]

        bio_infos = {}
        emails_final = []
        paypal = []
        for word in words:
            if "paypal.me/" in word:
                paypal.append(word)
            for i in emails:
                if i in word:
                    emails_final.append((word.split(i)[0]+i).lower())
        if len(emails_final) != 0:
            bio_infos['Emails'] = emails_final
        else:
            bio_infos['Emails'] = None
        if len(paypal) != 0:
            bio_infos['Paypals'] = paypal
        else:
            bio_infos['Paypals'] = None
        return bio_infos
    except AttributeError:
        return {'Emails':None,'Paypals':None}

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
            profiles.append(str(profile_formated))
    return profiles
