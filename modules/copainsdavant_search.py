import requests, bs4, colorama, json
from bs4 import BeautifulSoup

def copains_davant(name,pren):
    headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With':'XMLHttpRequest'
    }
    r = requests.get(url='http://copainsdavant.linternaute.com/s/?full=&q={} {}&ty=1&xhr='.format(pren,name),headers=headers)
    try:
        pagephone = r.content.decode().split(',"$data":')[1].split('{"copains":')[1]
        dataa = pagephone[:-2]
        data = json.loads(dataa)
        users_list = data['users']
        user_list = []
        for i in users_list:
            i = str(i).strip()
            if i != "0":
                user_list.append(i)
        new_verified = []
        for i in user_list:
            if len(new_verified) == 0:
                profile = data['users'][i]
                full_name = (profile['lib'])
                if name.lower() and pren.lower() in full_name.lower():
                    url =       (profile['url'])
                    new_verified.append(url)
        profil_url = new_verified[0]
        r = requests.get('http://copainsdavant.linternaute.com{}'.format(profil_url))
        pagephone = r.content
        featuresphone = "html.parser"
        soup = BeautifulSoup(pagephone,featuresphone)
        localisation = str(soup.find('span',{'class':'locality'}).text)
        naissance = str(soup.find('abbr',{'class':'bday'}).text.strip())
        name_full = str(soup.find('a',{'class':'url'}).text.strip())
        photo = str(soup.find('img',{'itemprop':'logo'})).split('itemprop="logo" src="')[1].split('"')[0]
        if "/anonymousL.jpg" in photo:
            photo = "None"
        card = soup.find('section',{'id':'vcard'}).text.strip()
        job = "None"
        nb_kids = "None"
        situation_familiale = "None"
        if "Situation familiale" in card:
            situation_familiale = card.split('Situation familiale :')[1].split(' ')[0].strip()
            situation_familiale = situation_familiale.strip()
        if "Profession" in card:
            job = card.split('Profession :')[1].split(' ')[0]
            job = " ".join(job.split()).split(' ')[0]
        if "Enfant" in card:
            nb_kids = card.split("Enfants :")[1].split(" ")[0]
        text = {'url_full':'http://copainsdavant.linternaute.com{}'.format(profil_url),'familial_situation':str(situation_familiale).replace('Enfants','').strip(),'full_name':str(name_full),'born':str(naissance),'localisation':str(localisation),
            "nb_enfants":str(nb_kids).strip(),"Job":str(job).strip(),'pdp':str(photo)         
        }
        return text
    except IndexError:
        return "None"
