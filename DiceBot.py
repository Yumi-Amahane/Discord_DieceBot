#!/usr/bin/env python
# coding: utf-8

# In[1]:


import discord
import random
import os

TOKEN=os.environ["Token"]#DiscordBotのトークンをいれておくこと

client = discord.Client()


# In[3]:


@client.event
async def on_message(message):
    if message.author.bot:
        return
             
    if (message.content[0]=="!" and message.content[1].isnumeric() and message.content.count("d")==1):
        MESS=message.content
        MESSsp=MESS[1:].split("d")
        if len(MESSsp)==2:
            if MESSsp[0].isnumeric() and MESSsp[1].isnumeric():
                N=int(MESSsp[0])
                R=int(MESSsp[1])
                RET=""
                WA=[]
                for i in range(N):
                    DEME=random.randint(1,R)
                    if R==10:
                        DEME-=1
                    RET+=str(DEME)+" "
                    WA.append(DEME)
                if MESS!="!2d10":
                    RET+=" :合計="+str(sum(WA))
                else:
                    RET+=":"+str(WA[0]*10+WA[1])+"%"
                await message.channel.send(RET)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)


# In[ ]:




