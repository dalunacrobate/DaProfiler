import threading, time, colorama, treelib, random, sys, os, argparse

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
from modules  import holehe_module

#from modules  import emailrep_io

from modules.api_modules import leakcheck_net
from modules.visual      import logging

banner = False 

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="Victim name")
parser.add_argument('-l','--logging',help="Enable terminal logging (Optional)")
parser.add_argument('-ln','--lastname',help="Last name of victim")
parser.add_argument('-e','--email',help="Email (Optional)")
parser.add_argument('-O','--output',help="( -O output.txt )")
args = parser.parse_args()

name     = (args.lastname)
pren     = (args.name)
log      = (args.logging)
email    = (args.email)
output   = (args.output)

if sys.platform == 'win32':
    os.system('cls')
else:
    os.system('clear')

print("Author : Dalunacrobate | Mail : "+Fore.CYAN+"daluna_pro@protonmail.ch\n"+Fore.RESET)
print("\r")

try:
    if pren and name is not None:
        logging.terminal_loggin(log,text=(" - Searching for Facebook accounts ...     \n"))
        facebook_results = facebook_search.facebook_search(name=name,pren=pren)
        logging.terminal_loggin(log,text=(" - Searching for Twitter accounts ...      \n"))
        twitter_results = twitter_search.twitter_search(name=name,pren=pren)
        logging.terminal_loggin(log,text=(" - Searching for Death records ...         \n"))
        avis_deces_results = death_records.death_search(name=name,pren=pren)
        logging.terminal_loggin(log,text=(" - Searching for Company ...               \n"))
        bfmtv_results = dirigeants_bfmtv.bfmtv_search(name=name,pren=pren)
        logging.terminal_loggin(log,text=(" - Searching for instagram accounts ...    \n"))
        instagram_results = instagram_search.ig_search(name=name,pren=pren)
        logging.terminal_loggin(log,text=(" - Searching for CopainsDavant accounts ...\n"))
        copainsdavant_results = copainsdavant_search.copains_davant(name=name,pren=pren)
        logging.terminal_loggin(log,text=(" - Searching for Skype accounts ...        \n"))
        skype_results = skype_search.skype_searchh(name=name,pren=pren)
        logging.terminal_loggin(log,text=(" - Searching for Phones and Adresses ...   \n"))
        pagesblanche = pagesblanches_search.adresse_search(name=name,pren=pren)
        logging.terminal_loggin(log,text=(" - Searching for Mail adresses ...         \n"))
        possible_mail = mail_gen.check(name=name,pren=pren)
        logging.terminal_loggin(log,text=(" - Searching for Mail from Skype ...       \n"))
        skype2mail = mail_gen.skype2email(name=name,pren=pren)
        logging.terminal_loggin(log,text=(" - Searching Leaked Passwords and social networks on emails ...       \n"))
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

print("\r")
tree = Tree()
tree.create_node(f"{pren} {name} {email}", 1)
if email_value == True:
    tree.create_node(email,15651145457841784,parent=1)
    logging.terminal_loggin(log,text=" - Searching for passwords via Scylla.soon target : {}\n".format(email))
    email_pass = scylla_sh.scylla_search(email=email)
    logging.terminal_loggin(log,text=" - Searching for passwords via LeakCheck.net API on target : {}\n".format(email))
    leakcheck_results = leakcheck_net.leak_check_api(mail=email)
    try:
        accs = holehe_module.social_scan(email=email)
        tree.create_node(Fore.MAGENTA+"Account Detection"+Fore.RESET,4594897841417,parent=15651145457841784)
        tree.create_node(accs,parent=4594897841417)
        if leakcheck_results is not None:
            tree.create_node(Fore.RED+"Passwords"+Fore.RESET+" : "+email,1296187151897415478411585,parent=15651145457841784)
            for i in leakcheck_results:
                chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                number_sk = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                tree.create_node(i['leak_name'],number_sk,parent=1296187151897415478411585)
                tree.create_node('Creditentials : {}'.format(i['password']),parent=number_sk)
                tree.create_node('Date : {}'.format(i['leak_date']),parent=number_sk)
        if len(email_pass) > 0:
            tree.create_node(Fore.RED+"Scylla.so"+Fore.RESET+" : "+email,49849489481858,parent=15651145457841784)
            for i in email_pass:
                chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                number_sk = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                tree.create_node('Scylla.sh',number_sk,parent=49849489481858)
                tree.create_node('Database : '+i['Name'],parent=number_sk)
                tree.create_node('Password : '+i['Password'],parent=number_sk)
    except TypeError:
        pass
if pagesblanche is not None:
    full_name = pagesblanche['Name']
    adress = pagesblanche['Adress']
    phone = pagesblanche['Phone']
    write("Adress - Phone : ",[str('Full Name : '+full_name),str('Adress : '+adress),str('Phone : '+phone)])
    tree.create_node(Fore.YELLOW+"Adress - Phone"+Fore.RESET,2,parent=1)
    tree.create_node("Full Name : {}".format(full_name),22,parent=2)
    tree.create_node("Adress    : {}".format(adress),33,parent=2)
    tree.create_node("Phone     : {}".format(phone),44,parent=2)
    if pagesblanche['carrier'] is not None:
        tree.create_node('Carrier : {}'.format(pagesblanche['carrier']),894,parent=44)
    if pagesblanche['Loc_phone'] is not None:
        tree.create_node('Localisation : {}'.format(pagesblanche['Loc_phone']),55,parent=44)
    if pagesblanche['Type_tel'] is not None:
        tree.create_node('Type  : {}'.format(pagesblanche['Type_tel']),66,parent=44)
if copainsdavant_results is not None:
    try:
        tree.create_node(Fore.RED+"Copains d'avant"+Fore.RESET,3,parent=1)
        tree.create_node('Full Name    : {}'.format(copainsdavant_results['full_name']),77,parent=3)
        tree.create_node('Born Date    : {}'.format(copainsdavant_results['born']),88,parent=3)
        tree.create_node('Location : {}'.format(copainsdavant_results['localisation']),99,parent=3)
        tree.create_node('Url          : {}'.format(copainsdavant_results['url_full']),111,parent=3)
        write('Copains d\'avant : ',[str('Full Name : '+copainsdavant_results['full_name']),str('Born Date : '+copainsdavant_results['born']),str('Location : '+copainsdavant_results['localisation']),str('URL : '+copainsdavant_results['url_full'])])
        if copainsdavant_results['pdp'] != "None":
            try:
                tree.create_node('Profile Picture : {}'.format(copainsdavant_results['pdp']),151515454545,parent=3)
            except:
                pass
        if copainsdavant_results['Job'] != "None":
            try:
                tree.create_node('Job : {}'.format(copainsdavant_results['Job']),154156132489411,parent=3)
            except:
                pass
        if copainsdavant_results['familial_situation'] != "None":
            try:
                tree.create_node('Familial Situation : {}'.format(copainsdavant_results['familial_situation'].strip()),44984154114515,parent=3)
            except:
                pass
        if copainsdavant_results['nb_enfants'] != "None":
            try:
                tree.create_node('Number of kids : {}'.format(copainsdavant_results['nb_enfants']),1654518948741,parent=3)
            except:
                pass
    except TypeError:
        pass
if bfmtv_results is not None:
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
    write(f'({str(len(twitter_results))}) Twitter : ',twitter_results)
    tree.create_node(Fore.CYAN+"Twitter"+Fore.RESET,5,parent=1)
    for i in twitter_results:
        tree.create_node(i,parent=5)
if skype_results is not None:
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
        write(f'({str(len(instagram_results))}) Instagram : ',instagram_results)
        tree.create_node(Fore.MAGENTA+"Instagram"+Fore.RESET,7,parent=1)
        tree.create_node('Accounts : {}'.format(str(len(instagram_results))),13,parent=7)
        for i in instagram_results:
            tree.create_node(i,parent=13)
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
                    # GETTING SITES WHERE EMAIL LOGGED IN FROM HOLEHE -> \modules\holehe_module.py
                    accs = holehe_module.social_scan(email=i)
                    if accs == "Accounts found : ":
                        pass
                    else:
                        chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                        number_soc = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                        tree.create_node(Fore.MAGENTA+"Account detection"+Fore.RESET,number_soc,parent=number)
                        tree.create_node(accs,parent=number_soc)
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
            write(f'({str(len(no_doubles))}) High Probability Emails : ',no_doubles)
        nb= str((len(possible_mail)))
        if int(nb) != 0:
            tree.create_node("("+Fore.YELLOW+nb+Fore.RESET+") "+Fore.YELLOW+"Possible Mailbox"+Fore.RESET,8,parent=146)
            write(f'({str(len(possible_mail))}) Possible Mailbox',possible_mail)
            for i in possible_mail:
                tree.create_node(i,parent=8)
if facebook_results is not None:
    write(f'({str(len(facebook_results))}) Facebook',facebook_results)
    nb = str(len(facebook_results))
    tree.create_node(Fore.BLUE+"Facebook"+Fore.RESET,9,parent=1)
    tree.create_node('Accounts : {}'.format(nb),10,parent=9)
    for i in facebook_results:
        tree.create_node(i,parent=10)
tree.show()
