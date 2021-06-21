from json import decoder
import threading, time, colorama, treelib, random, sys, os, argparse, json, requests, http.server, socketserver, webbrowser


from colorama import Fore, init, Back, Style
init(convert=True)
from treelib  import Node, Tree

from modules  import skype_search
from modules  import pagesblanches_search
from modules  import copainsdavant_search
from modules  import instagram_search
from modules  import dirigeants_bfmtv
from modules  import death_records
from modules  import twitter_search
from modules  import facebook_search
from modules  import mail_gen
from modules  import scylla_sh
from modules  import mail_check

from modules.api_modules import leakcheck_net
from modules.visual      import logging

banner = False 
# Opening json report template
data_file = open('modules/report.json','r')
data_export = json.load(data_file)
data_file.close()

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="Victim name")
parser.add_argument('-l','--logging',help="Enable terminal logging (Optional)")
parser.add_argument('-ln','--lastname',help="Last name of victim")
parser.add_argument('-e','--email',help="Email (Optional)")
parser.add_argument('-O','--output',help="( -O output.txt )")
parser.add_argument('-W','--webui',help='Open HTML report at the end')
args = parser.parse_args()

name     = (args.lastname)
pren     = (args.name)
log      = (args.logging)
email    = (args.email)
output   = (args.output)
web_arg  = (args.webui)

if sys.platform == 'win32':
    os.system('cls')
else:
    os.system('clear')

print("DaProfiler - Inspired from Profiler CToS")
print("Github : "+Fore.YELLOW+"https://github.com/dalunacrobate\n"+Fore.RESET)
print("Search in progress, please wait...")
print("\r")

possible_usernames = []

folder_name = "{}_{}".format(pren,name)

try:
    os.mkdir('Reports')
except FileExistsError:
    pass

try:
    os.mkdir('Reports/{}'.format(folder_name))
except FileExistsError:
    pass

personnal_life = []
social_medias  = []

try:
    if pren and name is not None:
        logging.terminal_loggin(log,text=("Searching for CopainsDavant accounts ...\n"))
        copainsdavant_results = copainsdavant_search.copains_davant(name=name,pren=pren)
        logging.terminal_loggin(log,text=("Searching for Facebook accounts ...     \n"))
        facebook_results = facebook_search.facebook_search(name=name,pren=pren)
        logging.terminal_loggin(log,text=("Searching for Twitter accounts ...      \n"))
        twitter_results = twitter_search.twitter_search(name=name,pren=pren)
        logging.terminal_loggin(log,text=("Searching for Death records ...         \n"))
        avis_deces_results = death_records.death_search(name=name,pren=pren)
        logging.terminal_loggin(log,text=("Searching for Company ...               \n"))
        try:
            bfmtv_results = dirigeants_bfmtv.bfmtv_search(name=name,pren=pren)
        except:
            bfmtv_results = None
        logging.terminal_loggin(log,text=("Searching for instagram accounts ...    \n"))
        instagram_results = instagram_search.ig_search(name=name,pren=pren)
        logging.terminal_loggin(log,text=("Searching for Skype accounts ...        \n"))
        skype_results = skype_search.skype_searchh(name=name,pren=pren)
        logging.terminal_loggin(log,text=("Searching for Phones and Adresses ...   \n"))
        pagesblanche = pagesblanches_search.adresse_search(name=name,pren=pren)
        logging.terminal_loggin(log,text=("Searching for Mail adresses ...         \n"))
        possible_mail = mail_gen.check(name=name,pren=pren)
        logging.terminal_loggin(log,text=("Searching for Mail from Skype ...       \n"))
        skype2mail = mail_gen.skype2email(name=name,pren=pren)
    elif len(pren) and len(name) == 0:
        facebook_results = None
        twitter_results = None
        avis_deces_results = None
        bfmtv_results = None
        instagram_results = None
        copainsdavant_results = None
        skype_results = None
        pagesblanche = None
        possible_mail = None
        skype2mail = None
        pren = ""
        name = ""
    else:
        facebook_results = None
        twitter_results = None
        avis_deces_results = None
        bfmtv_results = None
        instagram_results = None
        copainsdavant_results = None
        skype_results = None
        pagesblanche = None
        possible_mail = None
        skype2mail = None
        pren = ""
        name = ""
except TypeError:
    facebook_results = None
    twitter_results = None
    avis_deces_results = None
    bfmtv_results = None
    instagram_results = None
    copainsdavant_results = None
    skype_results = None
    pagesblanche = None
    possible_mail = None
    skype2mail = None
    pren = ""
    name = ""  

if email is not None:
    email_value = True
else:
    email = ""
    email_value = False

if output is not None:
    with open(output,'a+') as f:
        f.write('Results on target : {} {} {}\n\n'.format(name,pren,email))
        f.close()

def write(typee,objectt):
    if output is not None:
        with open(str(output),'a+',encoding='utf-8') as f:
            f.write('\n')
            if len(typee) == 0:
                pass
            else:
                f.write((typee)+"\n")
            for i in range(len(typee)):
                f.write('=')
            f.write('\n')
            if type(objectt) == list:
                for i in objectt:
                    f.write('- '+i+"\n")
            elif type(objectt) == str:
                f.write(objectt)

tree = Tree()
tree.create_node(f"{pren} {name} {email}", 1)
data_export['Name'] = pren
data_export['LastName'] = name
if email_value == True:
    tree.create_node(email,15651145457841784,parent=1)
    logging.terminal_loggin(log,text=" - Searching for passwords via Scylla.soon target : {}\n".format(email))
    logging.terminal_loggin(log,text=" - Searching for passwords via LeakCheck.net API on target : {}\n".format(email))
    leakcheck_results = leakcheck_net.leak_check_api(mail=email)
    try:
        if leakcheck_results is not None:
            tree.create_node(Fore.RED+"Passwords"+Fore.RESET+" : "+email,1296187151897415478411585,parent=15651145457841784)
            for i in leakcheck_results:
                chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                number_sk = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                tree.create_node(i['leak_name'],number_sk,parent=1296187151897415478411585)
                tree.create_node('Creditentials : {}'.format(i['password']),parent=number_sk)
                tree.create_node('Date : {}'.format(i['leak_date']),parent=number_sk)
    except TypeError:
        pass
if avis_deces_results is not None:
    tree.create_node("Death Records",41518181871541514778,parent=1)
    for i in avis_deces_results[:5]:
        tree.create_node('{}\t| {}'.format(i['Name'],i['Loc'][1:]),parent=41518181871541514778)
    data_export['DeathRecords']['Exists'] = True
    data_export['DeathRecords']['Records'] = avis_deces_results[:5]
if pagesblanche is not None:
    personnal_life.append('.')
    full_name = pagesblanche['Name']
    adress = pagesblanche['Adress']
    phone = pagesblanche['Phone']

    data_export['AdressPhone']['Exists'] = True    
    data_export['AdressPhone']['FullName'] = full_name
    data_export['AdressPhone']['Phone'] = phone
    data_export['AdressPhone']['Adress'] = adress

    write("Adress - Phone : ",[str('Full Name : '+full_name),str('Adress : '+adress),str('Phone : '+phone)])
    tree.create_node(Fore.YELLOW+"Adress - Phone"+Fore.RESET,2,parent=1)
    tree.create_node("Full Name : {}".format(full_name),22,parent=2)
    tree.create_node("Adress    : {}".format(adress),33,parent=2)
    tree.create_node("Phone     : {}".format(phone),44,parent=2)
    if pagesblanche['carrier'] is not None:
        tree.create_node('Carrier : {}'.format(pagesblanche['carrier']),894,parent=44)
    if pagesblanche['Loc_phone'] is not None:
        tree.create_node('Localisation : {}'.format(pagesblanche['Loc_phone']),55,parent=44)
        data_export['AdressPhone']['PhoneLocation'] = pagesblanche['Loc_phone']
    if pagesblanche['Type_tel'] is not None:
        tree.create_node('Type  : {}'.format(pagesblanche['Type_tel']),66,parent=44)
if copainsdavant_results is not None:
    personnal_life.append('.')
    data_export['CopainsDavant']['Exists'] = True
    try:
        tree.create_node(Fore.RED+"Copains d'avant"+Fore.RESET,3,parent=1)
        tree.create_node('Full Name    : {}'.format(copainsdavant_results['full_name']),77,parent=3)
        tree.create_node('Born Date    : {}'.format(copainsdavant_results['born']),88,parent=3)
        tree.create_node('Location : {}'.format(copainsdavant_results['localisation']),99,parent=3)
        tree.create_node('Url          : {}'.format(copainsdavant_results['url_full']),111,parent=3)
        
        data_export['CopainsDavant']['FullName']   = copainsdavant_results['full_name']
        data_export['CopainsDavant']['BornDate']   = copainsdavant_results['born']
        data_export['CopainsDavant']['ProfileUrl'] = copainsdavant_results['url_full'].replace('https://','')
        data_export['CopainsDavant']['Location']   = copainsdavant_results['localisation']

        write('Copains d\'avant : ',[str('Full Name : '+copainsdavant_results['full_name']),str('Born Date : '+copainsdavant_results['born']),str('Location : '+copainsdavant_results['localisation']),str('URL : '+copainsdavant_results['url_full'])])
        if copainsdavant_results['Other_locations'] is not None:
            chars = "abcdefghijklmnopqrstuvwxyz1234567890"
            number_sk = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
            tree.create_node('Other Locations',number_sk,parent=3)
            for i in copainsdavant_results['Other_locations']:
                if i != copainsdavant_results['localisation']:
                    tree.create_node(i,parent=number_sk)
            data_export['CopainsDavant']['OtherLocations'] = copainsdavant_results['Other_locations']
        if copainsdavant_results['pdp'] != "None":
            try:
                tree.create_node('Profile Picture : {}'.format(copainsdavant_results['pdp']),151515454545,parent=3)
                data_export['CopainsDavant']['ProfilePicUrl'] = copainsdavant_results['pdp'].replace('https://','')
            except:
                pass
        if copainsdavant_results['Job'] != "None":
            try:
                tree.create_node('Job : {}'.format(copainsdavant_results['Job']),154156132489411,parent=3)
                data_export['CopainsDavant']['Job'] = copainsdavant_results['Job']
            except:
                pass
        if copainsdavant_results['familial_situation'] != "None":
            try:
                tree.create_node('Familial Situation : {}'.format(copainsdavant_results['familial_situation'].strip()),44984154114515,parent=3)
                data_export['CopainsDavant']['FSituation'] = copainsdavant_results['familial_situation']
            except:
                pass
        if copainsdavant_results['nb_enfants'] != "None":
            try:
                tree.create_node('Number of kids : {}'.format(copainsdavant_results['nb_enfants']),1654518948741,parent=3)
                data_export['CopainsDavant']['NbKids'] = copainsdavant_results['nb_enfants']
            except:
                pass
    except TypeError:
        pass
if bfmtv_results is not None:
    personnal_life.append('.')
    data_export['Work']['Exists'] = True
    data_export['Work']['FullName'] = bfmtv_results['full_name']
    data_export['Work']['BornDate'] = bfmtv_results['naissance']
    data_export['Work']['Company']  = bfmtv_results['company']
    data_export['Work']['Function'] = bfmtv_results['fonction']
    data_export['Work']['Warrant']  = bfmtv_results['mandats']
    data_export['Work']['Link']     = bfmtv_results['link'].replace('https://','')

    write('Work - Job : ',[str('Adress : '+bfmtv_results['addr']),str('Company : '+bfmtv_results['company']),str('Full Name : '+bfmtv_results['full_name']),str('Function : '+bfmtv_results['fonction']),str('Warrant : '+bfmtv_results['mandats']),str('URL : '+bfmtv_results['link'])])
    tree.create_node(Fore.BLUE+"Work - Job"+Fore.RESET,4,parent=1)
    tree.create_node('Adress    : {}'.format(bfmtv_results['addr']),888,parent=4)
    tree.create_node('Company   : {}'.format(bfmtv_results['company']),777,parent=4)
    tree.create_node('Link      : {}'.format(bfmtv_results['link']),666,parent=4)
    tree.create_node('Full Name : {}'.format(bfmtv_results['full_name']),222,parent=4)
    tree.create_node('Born Date : {}'.format(bfmtv_results['naissance']),333,parent=4)
    tree.create_node('Function  : {}'.format(bfmtv_results['fonction']),444,parent=4)
    tree.create_node('Warrant   : {}'.format(bfmtv_results['mandats']),555,parent=4)
if twitter_results is not None:
    social_medias.append('.')
    data_export['Twitter']['Exists'] = True
    data_export['Twitter']['Accounts'] = twitter_results
    write(f'({str(len(twitter_results))}) Twitter : ',twitter_results)
    tree.create_node(Fore.CYAN+"Twitter"+Fore.RESET,5,parent=1)
    for i in twitter_results:
        tree.create_node(i,parent=5)
if skype_results is not None:
    social_medias.append('.')
    data_export['Skype']['Exists'] = True
    data_export['Skype']['AccountList'] = skype_results
    write(f'({str(len(skype_results))}) Skype : ',skype_results)
    tree.create_node(Fore.CYAN+"Skype"+Fore.RESET,6,parent=1)
    tree.create_node("Accounts : {}".format(str(len(skype_results))),12,parent=6)
    for i in skype_results:
        chars = "abcdefghijklmnopqrstuvwxyz1234567890"
        number_sk = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
        tree.create_node(i,number_sk,parent=12)
if instagram_results is not None:
    if len(instagram_results) ==  0:
        pass
    else:
        social_medias.append('.')
        data_export['Instagram']['Exists'] = True
        tree.create_node(Fore.MAGENTA+"Instagram"+Fore.RESET,7,parent=1)
        tree.create_node('Accounts : {}'.format(str(len(instagram_results))),13,parent=7)
        acc_json_list = []
        for i in instagram_results:
            chars = "abcdefghijklmnopqrstuvwxyz1234567890"
            username = i.split('|')[0].replace('@','').strip()
            number_ski = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
            bio_infos = instagram_search.getInstagramEmailFromBio(username)
            tree.create_node(i,number_ski,parent=13)
            data = instagram_search.get_extra_data(username)
            if data is not None:
                if data['obfuscated_email'] is not None:
                    ob_mail = data['obfuscated_email']
                    tree.create_node("Obfuscated Email -> "+ob_mail,parent=number_ski)
                else:
                    ob_mail = False
                if data['obfuscated_phone'] is not None:
                    ob_phone = data['obfuscated_phone']
                    tree.create_node("Obfuscated Phone -> "+ob_phone,parent=number_ski)
                else:
                    ob_phone = False
            else:
                ob_phone = False
                ob_mail  = False
            acc_json_list.append({"Username":username,'obfuscated_phone':ob_phone,'obfuscated_email':ob_mail})

            bio_emails = bio_infos['emails']
            paypal_bio = bio_infos['paypal']
            city_loc   = bio_infos['city_list']
            is_lgbt    = bio_infos['lgbt_points']
            schoolname = bio_infos['school']
            bestfriend = bio_infos['best_friend']
            love_date  = bio_infos['love_date']
            age_bio    = bio_infos['age']
            ethnicity  = bio_infos['origins']
            facebook_l = bio_infos['fb_list']
            twitter_l  = bio_infos['twitter_list']
            hobbies    = bio_infos['Hobbies']
            love_situa = bio_infos['love_situation']
            religions  = bio_infos['religions']
            astrologys = bio_infos['astrology']
            if love_situa is not None:
                nnumber_ski = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                tree.create_node('Love Situation',nnumber_ski,parent=number_ski)
                for i in love_situa:
                    tree.create_node(i,parent=nnumber_ski)
            if astrologys is not None:
                nnumber_ski = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                tree.create_node('Astrologic sign',nnumber_ski,parent=number_ski)
                for i in astrologys:
                    tree.create_node(i,parent=nnumber_ski)
            if religions is not None:
                nnumber_ski = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                tree.create_node('Religion(s)',nnumber_ski,parent=number_ski)
                for i in religions:
                    tree.create_node(i,parent=nnumber_ski)
            if hobbies is not None:
                nnumber_ski = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                tree.create_node('Hobbies',nnumber_ski,parent=number_ski)
                for i in hobbies:
                    tree.create_node(i,parent=nnumber_ski)
            if bestfriend is not None:
                nnumber_ski = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                tree.create_node('Good relationship with',nnumber_ski,parent=number_ski)
                for i in bestfriend:
                    tree.create_node('{}'.format(i),parent=nnumber_ski)
            if is_lgbt is not None:
                lgbt_flag = (Fore.RED+"█"+Fore.YELLOW+"█"+Fore.GREEN+"█"+Fore.BLUE+"█"+Fore.MAGENTA+"█"+Fore.RESET)
                tree.create_node('{} LGBT Member'.format(lgbt_flag),parent=number_ski)
            if ethnicity is not None:
                tree.create_node('Ethnicity : {}'.format(str(ethnicity).replace('[','').replace(']','').replace("'","")),parent=number_ski)
            if facebook_l is not None:
                tree.create_node('Facebook : {}'.format(str(facebook_l).replace('[','').replace(']','').replace("'","")),parent=number_ski)
            if twitter_l is not None:
                tree.create('Twitter : {}'.format(str(twitter_l).replace('[','').replace(']','').replace("'","")),parent=number_ski)
            if schoolname is not None:
                tree.create_node('School Name : {}'.format(schoolname),parent=number_ski)
            if city_loc is not None:
                tree.create_node('City : {}'.format(city_loc[0]),parent=number_ski)
            if paypal_bio is not None:
                for i in paypal_bio:
                    tree.create_node('Paypal in bio -> '+i,parent=number_ski)
            if bio_emails is not None:
                for i in bio_emails:
                    write('Searching infos on ',i)
                    chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                    number_skkk = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                    number_skk = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                    tree.create_node('Email from bio -> '+Fore.CYAN+i+Fore.RESET,number_skkk,parent=number_ski)
        data_export['Instagram']['AccountList'] = acc_json_list
if possible_mail is not None:
    if len(possible_mail) != 0 or len(skype2mail) != 0:
        tree.create_node(Fore.RED+'Emails extracted'+Fore.RESET,146,parent=1)
        if skype2mail is not None:
            tree.create_node('['+Fore.GREEN+"++"+Fore.RESET+'] High probability',142,parent=146)
            no_doubles = []
            for i in skype2mail:
                if i not in no_doubles:
                    chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                    number = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                    no_doubles.append(i)
                    tree.create_node(i,number,parent=142)
                    # GETTING LEAKED PASSWORDS FROM SCYLLA.SH -> \modules\scylla_sh.py
                    scylla_results = scylla_sh.scylla_search(email=i)
                    if scylla_results is not None:
                        tree.create_node(Fore.RED+'Leaked From'+Fore.RESET+' : Scylla.sh',1518451,parent=number)
                        for i in scylla_results:
                            chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                            number = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                            tree.create_node('Leak Name : {}'.format(i['Name']),parent=1518451)
                            tree.create_node('Password  : {}'.format(i['Password']),parent=1518451)
                    # GET LEAKED PASSWORDS FROM LEAKCHET.NET API -> \api_modules\leakcheck_net.py
                    a = leakcheck_net.leak_check_api(mail=i)
                    if a is not None:
                        chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                        number_pass = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                        tree.create_node(Fore.RED+Back.WHITE+"Leaked Creditentials"+Fore.RESET+Style.RESET_ALL,number_pass,parent=number)
                        for i in a:
                            password  = i['password']
                            leak_name = i['leak_name']
                            leak_date = i['leak_date']
                            tree.create_node('Password  : {}'.format(password),parent=number_pass)
                            tree.create_node('Leak Name : {}'.format(leak_name),parent=number_pass)
                            tree.create_node('Leak Date : {}'.format(leak_date),parent=number_pass)
            data_export['Emails']['HighProbEmails'] = no_doubles
            write(f'({str(len(no_doubles))}) High Probability Emails : ',no_doubles)
        nb= str((len(possible_mail)))
        if int(nb) != 0:
            tree.create_node("("+Fore.YELLOW+nb+Fore.RESET+") "+Fore.YELLOW+"Possible Mailbox"+Fore.RESET,8,parent=146)
            write(f'({str(len(possible_mail))}) Possible Mailbox : ',possible_mail)
            data_export['Emails']['PermutatedMailbox'] = possible_mail
            for i in possible_mail:
                tree.create_node(i,parent=8)
if facebook_results is not None:
    social_medias.append('.')
    data_export['Facebook']['Exists'] = True
    write(f'({str(len(facebook_results))}) Facebook : ',facebook_results)
    nb = str(len(facebook_results))
    tree.create_node(Fore.BLUE+"Facebook"+Fore.RESET,9,parent=1)
    tree.create_node('Accounts : {}'.format(nb),10,parent=9)
    data_export['Facebook']['AccountList'] = facebook_results
    for i in facebook_results:
        tree.create_node(i,parent=10)
tree.show()

data_export['UI']['Pie']['PersonnalLife']   = len(personnal_life)
data_export['UI']['Pie']['SocialMedias']    = len(social_medias)
try:
    data_export['UI']['Bar']['TwitterFounds']   = len(twitter_results)
except TypeError:
    data_export['UI']['Bar']['TwitterFounds']   = 0
try:
    data_export['UI']['Bar']['InstagramFounds'] = len(instagram_results)
except TypeError:
    data_export['UI']['Bar']['InstagramFounds'] = 0
try:
    data_export['UI']['Bar']['FacebookFounds']  = len(facebook_results)
except TypeError:
    data_export['UI']['Bar']['FacebookFounds']  = 0
try:
    data_export['UI']['Bar']['SkypeFounds']     = len(skype_results)
except TypeError:
    data_export['UI']['Bar']['SkypeFounds']     = 0
    
data_file.close()

try:
    with open(f'Reports/{folder_name}/{name}_{pren}.json','w',encoding='utf8') as f:
        json.dump(data_export,f,indent=4,ensure_ascii=False)
        f.close()
except FileNotFoundError:
    os.mkdir('Reports')
    with open(f'Reports/{folder_name}/{name}_{pren}.json','w',encoding='utf8') as f:
        json.dump(data_export,f,indent=4,ensure_ascii=False)
        f.close()

def webui():
    url = 'https://cnil.me/api/osint/daprofiler/ui'
    myobj = json.dumps(data_export)
    x = requests.post(url, data = myobj)
    y = json.loads(x.text) 
    print("Website Done")
    f = open("./web/index.html", "w")
    f.write(y['content']["webpage"])
    f.close()
    f = open("./web/cg/data.json", "w")
    f.write(y['content']["arbre"])
    f.close()
    Handler = http.server.SimpleHTTPRequestHandler

    webbrowser.open('http://127.0.0.1:8000/web/', new=2)
    with socketserver.TCPServer(("", 8000), Handler) as httpd:
        print("serving at port", 8000)
        httpd.serve_forever()

if web_arg is not None:
    webui()
