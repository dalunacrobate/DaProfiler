"""
This module belongs to Magadose.
This module is under GPL3.0 -> https://www.gnu.org/licenses/gpl-3.0.fr.html

OWNER CONTACT INFOS :
======================
Twitter : @palenath
Github : https://github.com/megadose
Holehe repo : https://github.com/megadose/holehe
BTC Adress for donations : 1FHDM49QfZX6pJmhjLE5tB2K6CaTLMZpXZ
"""
import holehe, httpx, trio

from holehe.modules.social_media.tellonym   import *
from holehe.modules.social_media.bitmoji    import *
from holehe.modules.social_media.crevado    import *
from holehe.modules.social_media.discord    import *
from holehe.modules.social_media.instagram  import *
from holehe.modules.social_media.xing       import *
from holehe.modules.social_media.vsco       import *
from holehe.modules.social_media.twitter    import *
from holehe.modules.social_media.wattpad    import *
from holehe.modules.social_media.snapchat   import *
from holehe.modules.social_media.myspace    import *
from holehe.modules.social_media.pinterest  import *
from holehe.modules.social_media.taringa    import *
from holehe.modules.social_media.imgur      import *

from holehe.modules.programing.github        import *

from holehe.modules.transport.blablacar import *

from holehe.modules.music.lastfm   import *
from holehe.modules.music.spotify  import *
from holehe.modules.music.smule    import *
from holehe.modules.music.tunefind import *

from holehe.modules.porn.pornhub  import *
from holehe.modules.porn.redtube  import *
from holehe.modules.porn.xvideos  import *

from holehe.modules.shopping.ebay      import *
from holehe.modules.shopping.amazon    import *
from holehe.modules.shopping.dominosfr import *
from holehe.modules.shopping.deliveroo import *

def social_scan(email):
    accounts_list = []
    async def ebayy():
        out = []
        client = httpx.AsyncClient()
        await ebay(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def amazonn():
        out = []
        client = httpx.AsyncClient()
        await amazon(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def deliverooo():
        out = []
        client = httpx.AsyncClient()
        await deliveroo(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def dominoss():
        out = []
        client = httpx.AsyncClient()
        await dominosfr(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def redutbee():
        out = []
        client = httpx.AsyncClient()
        await redtube(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def pornhubb():
        out = []
        client = httpx.AsyncClient()
        await pornhub(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def xvideoss():
        out = []
        client = httpx.AsyncClient()
        await xvideos(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def tunefindd():
        out = []
        client = httpx.AsyncClient()
        await tunefind(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def smulee():
        out = []
        client = httpx.AsyncClient()
        await smule(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def lasfmm():
        out = []
        client = httpx.AsyncClient()
        await lastfm(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def spotifyy():
        out = []
        client = httpx.AsyncClient()
        await spotify(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def blablacarr():
        out = []
        client = httpx.AsyncClient()
        await blablacar(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def imgurr():
        out = []
        client = httpx.AsyncClient()
        await imgur(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def taringaa():
        out = []
        client = httpx.AsyncClient()
        await taringa(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def pinterestt():
        out = []
        client = httpx.AsyncClient()
        await pinterest(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def myspacee():
        out = []
        client = httpx.AsyncClient()
        await myspace(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def snapchatt():
        out = []
        client = httpx.AsyncClient()
        await snapchat(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def wattpadd():
        out = []
        client = httpx.AsyncClient()
        await wattpad(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def twitterr():
        out = []
        client = httpx.AsyncClient()
        await twitter(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def instagramm():
        out = []
        client = httpx.AsyncClient()
        await instagram(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def discordd():
        out = []
        client = httpx.AsyncClient()
        await discord(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def crevadoo():
        out = []
        client = httpx.AsyncClient()
        await crevado(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def bitmojii():
        out = []
        client = httpx.AsyncClient()
        await bitmoji(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def snapchatt():
        out = []
        client = httpx.AsyncClient()
        await snapchat(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    async def githubb():
        out = []
        client = httpx.AsyncClient()
        await github(email, client, out)
        accounts_list.append(out)
        await client.aclose()
    
    trio.run(githubb)
    trio.run(snapchatt)
    trio.run(bitmojii)
    trio.run(crevadoo)
    trio.run(discordd)
    trio.run(dominoss)
    trio.run(instagramm)
    trio.run(wattpadd)
    trio.run(twitterr)
    trio.run(myspacee)
    trio.run(imgurr)
    trio.run(taringaa)
    trio.run(blablacarr)
    trio.run(deliverooo)
    trio.run(spotifyy)
    trio.run(smulee)
    trio.run(tunefindd)
    trio.run(lasfmm)
    trio.run(redutbee)
    trio.run(pornhubb)
    trio.run(xvideoss)
    trio.run(ebayy)
    trio.run(amazonn)
    accounts_ok = []
    for i in accounts_list:
        try:
            if i[0]['exists'] == True:
                accounts_ok.append(i[0]['name'])
        except:
            pass
    a = accounts_ok
    founds = ('Accounts found : '+str(a).replace('[','').replace(']','').replace("'",""))
    return founds
