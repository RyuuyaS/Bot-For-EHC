import os
import discord
from dotenv import load_dotenv
import asyncio
load_dotenv()
from utils import functions as util

class port443:
    ############# set up variable #######################################################
    host = "antoine@192.168.0.0"
    HTML = '''
    <!DOCTYPE html>
       <html lang="en">
         <head>
           <meta charset="UTF-8">
           <meta name="viewport" content="width=device-width, initial-scale=1.0">
           <meta http-equiv="X-UA-Compatible" content="ie=edge">
           <link rel="stylesheet" href="style.css">
           <title>On Includes</title>
         </head>
         <body>
           <script src="script.js"></script>
            <!-- you can open file script.js and style.css -->
           <h1>My Life as Terror</h1>
           <p>The greater the suffer, the greater the piece.</p>
           <br>
           <p> Source: EHC </p>
           <button type="button" onclick="greetings();">Say hello</button>
         </body>
       </html>
    '''
    CSS = '''
    body {
        background-color: lightblue;
        /* NO1} */
          }'''
    JS = '''function detonate()
     {
       alert("Self destructed!");
     }'''
    YOUTUBE = 'NB2HI4DTHIXS653XO4XHS33VOR2WEZJOMNXW2L3XMF2GG2B7OY6WIULXGR3TSV3HLBRVC==='
    WEBSITE = 'antoineHackerLord.com'
    FINALE = """
    - COMPLETED ATTACKS: 
        +) 29/02/2019: SPREAD OUT CORONA VIRUS
        +) 20/10/2020: HIJACK INTERNATIONAL AIRPLANE IN CHINA
        +) 09/11/2021: BOMB AT EIFEL TOWER IN FRANCE

    - PLANNING ATTACKS: 
        +) 26/11/2022 AT ********* ********* (FOR SECURITY REASON ONLY SHOW THE ENCODED IMAGE)"""
   
##################################################################################################
    def __init__(self):
        pass

    async def loginCheck(self, ctx):
        await ctx.send(util.syntaxHighlight(f"Login to {self.host} 443 successfully\n",""))
        return True

    async def listAllFile(self, ctx):
        await ctx.send(util.syntaxHighlight("1. base.html\n2. test.antoineHackerLord.com\n",""))

    async def xdg_open(self, ctx, fileName: str):
        if fileName == 'base.html':
            await ctx.send(embed=util.embedColor(self.HTML,"html","FILE: base.html"))
        elif fileName == 'script.js':
            await ctx.send(embed=util.embedColor(self.JS,"js","FILE: script.js"))
        elif fileName == 'style.css':
            await ctx.send(embed=util.embedColor(self.CSS,"css","FILE: style.css"))
            await asyncio.sleep(5)
            string = '''Congrats on finding the nuclear key, you have done well. However, we worry that he would change the attack but still happen at the same location.\nYour final mission is to find the document file containing information about that attack and find the exact name of the place where it takes place.
            '''
            await ctx.send(embed=util.embedColor(string,"","FINAL MISSION"))
            await asyncio.sleep(3)
            string = "Our spy tells us that maybe it is hidden at the current directory. You should check it.\nRemember that you only have 5 minutes left before Antoine finds out everything. Good luck !\n(P/s: Maybe this could help you: https://devconnected.com/how-to-show-hidden-files-on-linux/. Anyway, the command is: ls -a 😜)"
            await ctx.send(embed=util.embedColor(string,"","HINT FOR YOU"))

        elif fileName == 'test.antoineHackerLord.com':
            await ctx.send(embed=util.embedColor("NOTHING HERE","","FILE: test.antoineHackerLord.com"))
        elif fileName == '.secret.txt':
            await ctx.send(embed=util.embedColor(self.YOUTUBE,"","FILE: .secret.txt"))
            await ctx.send(util.syntaxHighlight("Oh, another encryption. Looks like Base64 but it isn't. Perhaps, Base 64/2=? ",""))
        elif fileName == '.nothing_special_here.txt':
            await ctx.send(embed=util.embedColor(self.FINALE,"","FILE: .nothing_special_here.txt"))
            await ctx.send(file=discord.File('D:\Download\DiscordBot_EHC_Workshop\chall_QR.png'))
        else:
            await ctx.send(embed=util.embedColor("- No such file exist - ","diff","ERROR"))
        return True

    async def listAllHiddenFile(self, ctx):
        await ctx.send(util.syntaxHighlight("1. base.html\n2. test.antoineHackerLord.com\n3. .secret.txt\n 4. .nothing_special_here.txt",""))
