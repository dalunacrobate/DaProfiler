[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html) [![Open Source Love svg3](https://badges.frapsoft.com/os/v3/open-source.svg?v=103)](https://github.com/dalunacrobate/daprofiler)
![](https://visitor-badge.laobi.icu/badge?page_id=dalunacrobate.daprofiler)

**EN** : For educational purposes only.

![alt text](https://i.ibb.co/5xhj7pZ/8b9770d14be1d8c3f86d157d32d4044e.png)
# DaProfiler

**EN** DaProfiler allows you to create a profile on your **target** based in France only.
The particularity of this program is its ability to find the e-mail addresses of a target via searches on [Skype](https://www.skype.com/) and tests of combining e-mail addresses followed by a check to know if the email address exists or not (Beware of false negatives, the results displayed do not necessarily relate to the target you are looking for if another person has the same name - first name). DaProfiler is also able to check the words of a an instagram bio to find interesting information such as : **Email addresses**, **Paypal.me profiles**,**Sexual Orientation**,**City**,**School**,**Age**,**Ethnicity**,**Religions**,**Hobbies** and more ...

## 🛠 Installation - Linux

Python 3.8 required
```bash
git clone https://github.com/dalunacrobate/DaProfiler.git
cd DaProfiler
pip install -r requirements.txt
```
## 💻 Use
```bash
usage: profiler.py [-h] [-n NAME] [-l LOGGING] [-ln LASTNAME] [-e EMAIL] [-O OUTPUT] [-W WEBUI]

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Victim name
  -l LOGGING, --logging LOGGING
                        Enable terminal logging (Optional)
  -ln LASTNAME, --lastname LASTNAME
                        Last name of victim
  -e EMAIL, --email EMAIL
                        Email (Optional)
  -O OUTPUT, --output OUTPUT
                        ( -O output.txt )
  -W WEBUI, --webui WEBUI
                        Open HTML report at the end
```

## 📷 Demo
![alt text](https://i.ibb.co/YPHwv39/hh.png)

## 🛠 Api
| Source | Service type | Subscription | Key in code |
| :---: | :---: | :---: | :---: |
| emailrep.io | Email Reputation | Free ✅ | No Key |
| Leakcheck.net | Breach Search | Premium 🔑 | ❌ | 
| apilayer.net | Phone infos | Free ✅ | ✅ |
| Scylla | Breach Search | Free ✅ | No Key |

Add your premium api keys :
+ Go to [modules\api_modules](https://github.com/dalunacrobate/DaProfiler/tree/main/modules/api_modules) then open your API module (ex Leakcheck), replace "YOUR_KEY" to your key, save and quit your text editor.

##  📝 Contact
Mail : _daluna_pro@protonmail.ch_. <br>
Discord : `Dalunacrobate#6166` <br>
Discord server : [https://discord.gg/2RStanwK2S](https://discord.gg/2RStanwK2S)


## 📚 Contributions
All suggestions are welcome.

![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)

