from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import Location
from akad.ttypes import ChatRoomAnnouncement
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
#from gtts import gTTS
_session = requests.session()
botStart = time.time()
settingsOpen = codecs.open("Abouts.json","r","utf-8")
Abouts = json.load(settingsOpen)
#====== Akun Self ===========
print ("Memuat Akun Selfbot")
#me = LINE() #Login Via QR
me = LINE("EB4J1aHSwrTGmnemgo2f.BnRtomZJWFsv+6Vt2XUFFW.GeUlfQQFcnDI9h6d52o2DqO91t3/oCPdlXA1sOzF4nU=")
me.log("\nToken Selfbot=> " + str(me.authToken))
channelToken = me.getChannelResult()
print ("Sukses Login Akun Selfbot")
#====== Akun BOT 1 ==========
print ("Memuat Akun Bot 1")
#bot1 = LINE()
bot1 = LINE("EBkojlzXFic3IQYXWpL2.PItg9+itWKU99vYJNtK/0G.YLkysg2RyMaMToU6ChaBfEVVJjtKxOc+ydzro53p4Ds=")
bot1.log("\nToken Bot 1=> " + str(bot1.authToken))
print ("Sukses Login Akun BOT 1")
#====== Akun BOT 2 ==========
print ("Memuat Akun Bot 2")
#bot2 = LINE()
bot2 = LINE("EBrDqnanZbxjSlGvkNl4.XFO6RBvtyWrQAVOEOUKVDa./jSOi54WQgt4dEIW3mkl+IEZ7IIfZV8jeFGV8J5+XC8=")
bot2.log("\nToken Bot 2=> " + str(bot2.authToken))
print ("Sukses Login Akun BOT 2")
#====== Akun BOT 3 ==========
print ("Memuat Akun Bot 3")
#bot3 = LINE()
bot3 = LINE("EBAGxkd2xju0z3M3lav2.KNyFu70vZ7rFM/hPKfWtCG.JJVraY564m6m86kZ/9XNYl2BeVP2UBPHnV+Cn/8hAF4=")
bot3.log("\nToken Bot 3=> " + str(bot3.authToken))
print ("Sukses Login Akun BOT 3")
#====== Akun BOT 4 ==========
print ("Memuat Akun Bot 4")
#bot4 = LINE()
bot4 = LINE("EBCd8pe05YmLxua1yzj8.6ahqKyDkfHEyPKBLa3Xjca.v1SR3hEv1OTXwqDD4qm+RrnMjxQzT9HRoJOrXp/be7I=")
bot4.log("\nToken Bot 4=> " + str(bot4.authToken))
print ("Sukses Login Akun BOT 4")
#====== Akun BOT 5 ==========
print ("Memuat Akun Bot 5")
#bot5 = LINE()
bot5 = LINE("EBsCaurbRrkbG9c0DCle.Tev1+QLCpnGlJYFt6DxZRG.fWpo6uKlGKL7XWFbjg7w6YE2no7Wk3pJEDUG4vu9T8A=")
bot5.log("\nToken Bot 5=> " + str(bot5.authToken))
print ("Sukses Login Akun BOT 5")
#====== Akun BOT 6 ==========
print ("Memuat Akun Bot 6")
#bot6 = LINE()
bot6 = LINE("EBQ70MJLTASon4kUOEi2.IZE5ypV8qavBNVsRSLn7GG.A9nXYyeXCjmXEHqqTRtoyk+dH9z1Ws3jzfR06muja38=")
bot6.log("\nToken Bot 6=> " + str(bot6.authToken))
print ("Sukses Login Akun BOT 6")
#====== Akun BOT 7 ==========
print ("Memuat Akun Bot 7")
#bot7 = LINE()
bot7 = LINE("EBTaX1SScYlEWw0yuaFa.q+Ks6PqMcbadP5cl5U4N/G.WJel5Ds4cAU8tHjnWlt+jhNz0Ymx9XCWCZZiaRh4f6E=")
bot7.log("\nToken Bot 7=> " + str(bot7.authToken))
print ("Sukses Login Akun BOT 7")
#====== Akun BOT 8 ==========
print ("Memuat Akun Bot 8")
#bot8 = LINE()
bot8 = LINE("EBW6zLLH3UbJGuSZmWL8.FSdiXI4nR1/1uLI2n+Qwka.I2iShGMsaAot1JWGAjR+vMKczMrdGp0VsC01Ju20JOk=")
bot8.log("\nToken Bot 8=> " + str(bot8.authToken))
print ("Sukses Login Akun BOT 8")
#====== Akun Anti JS 1==========
print ("Memuat Akun Anti JS 1")
#Java_script = LINE()
Java_script = LINE("EBhSj0yjlPT0B3ZpRc25.n6d72ILyL2Z7/JCLUk7DPq.PJLqo/DZeX8OQClrEVtmz0LjJoKscsZNx5egSqnJ6ZM=")
Java_script.log("\nToken AntiJS 1=> " + str(Java_script.authToken))
print ("Sukses Login Akun AntiJS 1")
#====== Akun Anti JS 2==========
print ("Memuat Akun Anti JS 2")
#Java_script2 = LINE()
Java_script2 = LINE("EBsV2E4usxFmspYvq3H8.OwwWRyvFrDmAlz5r16m2Ya.Zr9mDfSkQLCmA2yAxl1xYpjkSEo19CPxoH85Koc6+Kc=")
Java_script.log("\nToken AntiJS 2=> " + str(Java_script2.authToken))
print ("Sukses Login Akun AntiJS 2")
#===================================================
print ("Sukses Menjalankan Semua BOT !!!")
print ("╔════════════════════════════════")
print ("║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓")
print ("║   ★‡Bot Siap Digunakan★")
print ("║   Script Dasar Created By : Alphat Team JS")
print ("║   Script Edited By : One Piece Team")
print ("║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓")
print ("║ ⭐Ｏｎｅ ｐｉｅｃｅ Ｔｅａｍ⭐")
print ("║  → Owner 1 : Hanavy Koplax's")
print ("║  → Owner 2 : Prasetyo")
print ("║  → Editor Text : Luki")
print ("║  → Testing Script : Yandi")
print ("║  → Donatur : Adam")
print ("║  → Dan Terima Kasih Untuk Semua Anggota")
print ("╚════════════════════════════════")
#============================================
Java_scriptRanger = Java_script.profile.mid
Java_scriptProfile = Java_script.getProfile()
Java_scriptSettings = Java_script.getSettings()
Java_script2Ranger = Java_script2.profile.mid
Java_script2Profile = Java_script2.getProfile()
Java_script2Settings = Java_script2.getSettings()
BotRanger = bot1.profile.mid
BotRangerProfile = bot1.getProfile()
BotRangerSettings = bot1.getSettings()
BotRanger2 = bot2.profile.mid
BotRanger2Profile = bot2.getProfile()
BotRanger2Settings = bot2.getSettings()
BotRanger3 = bot3.profile.mid
BotRanger3Profile = bot3.getProfile()
BotRanger3Settings = bot3.getSettings()
BotRanger4 = bot4.profile.mid
BotRanger4Profile = bot4.getProfile()
BotRanger4Settings = bot4.getSettings()
BotRanger5 = bot5.profile.mid
BotRanger5Profile = bot5.getProfile()
BotRanger5Settings = bot5.getSettings()
BotRanger6 = bot6.profile.mid
BotRanger6Profile = bot6.getProfile()
BotRanger6Settings = bot6.getSettings()
BotRanger7 = bot7.profile.mid
BotRanger7Profile = bot7.getProfile()
BotRanger7Settings = bot7.getSettings()
BotRanger8 = bot8.profile.mid
BotRanger8Profile = bot8.getProfile()
BotRanger8Settings = bot8.getSettings()
meM = me.profile.mid
meProfile = me.getProfile()
meSettings = me.getSettings()
oepoll = OEPoll(me)
Owner = [
  "u6cdad338cce3c1f495ffabd3db1b9f7f", #Aku
  "uc8f8563caca94440db988429fbc20e59", #Bebkuh
  "u3846b76f3fc3bcedd70f6e47375db6eb", #Ainy
  "u1d5d95747a3d93679e3a1da1f0897d91", #Atik
  "u7126fc36e62a50b69607b157b8a01e41", #Piyan
  "u4db911da421cbba2e1527c129b5f2d1c", #Kemprut
  "u36ba9f0c94e4254fa4040d16c58e01f6", #Kiki
  "u672ef7328c61d3538900bb2cec4b9352", #GAGown1
  "u983ef9e3b1eff0dfa14fe134863c5a06", #GAGown2
  "u85727f2915016b24940b09c7d8e3dafc", #Suci LYR
  "ue8536c2dae1b9c13b7c4e042e7ef8a6d", #Nelly LYR
  "u019c76b8366990aa14ea686cc1b17a05", #Bagus LYR
  "u48aa90696418296626258a2cf32f073b"] #Ari LYR
Bots = [meM,BotRanger,BotRanger2,BotRanger3,BotRanger4,BotRanger5,BotRanger6,BotRanger7,BotRanger8,Java_scriptRanger,Java_script2Ranger,Owner]
KACOP = [bot1,bot2,bot3,bot4,bot5,bot6,bot7,bot8]
KACJS = [Java_script,Java_script2]
Stiles = "│™│ "
respontags = {
    "Auto_text":"\nNah Kan, Ngetag\nAwas Naksir?"
}
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
Sid={
    "Tar":{},
    "Red":{},
    "Reason":{}
}
mid = me.getProfile().mid
wait={
    "lang":"JP",
    "key": False,
    "text": "Bot:",
    "Sambutan":True,
    "contact":False,
    "AddFriend":False,
    "autoAdd":True,
    "Protectkick":True,
    "pname":{},
    "pro_name":{},
    "ProtectInvite":True,
    "ProtectQR":True,
    "Protectcancel":True,
    "checkContact": False,
    "bot": True,
    "Conection": True,
    "Add": False,
    "Join": False,
    "Wc": False,
    "Shared": False,
    "Respon": False,
    "Read": False,
    "Unsend": False,
    "blacklist": {},
    "PROTECT": [
       "c390b17f9b8749ffac5a30f8346497218", # GAG
       "ce2ed6c13c9f02e77b55e601fb71c29c0", #RBT
       "c28f663b5bdaa90cbff577fe7cee48ff9", #GSS
       "c9b4e6c2de57f0f20d96c035bdd9c836f" #ROOM BOT
    ],
    "myProfile": {
        "coverId": "",
        "displayName": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "addadmin":False,
    "delladmin":False,
    "banAdd":False,
    "banDel":False,
    "Sider":{}
}
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
#========================================================
wait["myProfile"]["displayName"] = meProfile.displayName
wait["myProfile"]["statusMessage"] = meProfile.statusMessage
cont = me.getContact(meM)
wait["myProfile"]["pictureStatus"] = meProfile.pictureStatus
coverId = me.getProfileDetail()["result"]["objectId"]
apikey_com = "ubaba90be636d918cab5509685cef5c23" #u0ac948397fbc732bd3bc5ca273faa698
coverId = me.getProfileDetail()["result"]["objectId"]
wait["myProfile"]["coverId"] = coverId
Extr = me.getContact(apikey_com).displayName
def backupData():
    try:
        #backup = AntiJS
        #f = codecs.open('AntiJS.json','w','utf-8')
        #json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = Abouts
        f = codecs.open('Abouts.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        ErrorX(error)
        return False
def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Tag User「{}」\n\n  [ Tag ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(me.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        me.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        me.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def sendMeention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@Woy "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    me.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def Run_Xp():
    print ("RESTART")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
Devert = "My name is "+cont.displayName+"\nMy git your bots"
def Run_Xx():
    print ("BOT KEMBALI AKTIF")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
mulai = time.time()
def Musik(to):
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+me.getContact(meM).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': me.getContact(meM).statusMessage if me.getContact(meM).statusMessage != '' else 'creator By Hanavy Koplaxs |ID LINE|\hanavy1992', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': me.getContact(meM).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+meM,'MSG_SENDER_NAME':  me.getContact(meM).displayName,}
    return me.sendMessage(to, me.getContact(meM).displayName, contentMetadata, 19)
def ErrorX(text):
    me.log("data: " + str(text))
    time_ = datetime.now()
    with open("Data.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMeention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@Woy "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    me.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        me.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        ErrorX(error)
        me.sendMessage(to, "Error\n\n" + str(error))
extras = Stiles+"Creator:by "+Extr+"\n"
def RunTheRun(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,7,25)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = me.getAllContactIds()
        gid = me.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        h = me.getContact(meM)
        me.reissueUserTicket()
        My_Id = "http://line.me/ti/p/"+me.getUserTicket().id
        text += mention+"WAKTU : "+datetime.strftime(timeNow,'%H:%M:%S')+" INDONESIA\n\nMY GROUP : "+str(len(gid))+"\n\nMY FRIEND: "+str(len(teman))+"\n\nTIME VPS : In "+hari+"\n\nᴄʀᴇᴀᴛᴏʀ ʙʏ : ᴘʀᴀɴᴋʙᴏᴛs. ʟɪɴᴇ ᴠᴇʀ.8.14.2\n\nTANGGAL : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n\nTIME RUN : \n • "+bot+"\n\nMY TOKEN : "+str(me.authToken)+"\n\nMY MID : "+h.mid+"\n\nMY ID LINE : "+My_Id
        me.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        me.sendMessage(to, "Error :\n" + str(error))
def SqL_R(text):
    R_SQL = text.lower()
    if wait["key"] == True:
        if R_SQL.startswith(wait["text"]):
            WaitData = R_SQL.replace(wait["text"],"")
        else:
            WaitData = "Undefined command"
    else:
        WaitData = text.lower()
    return WaitData
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 26 or op.type == 25:
            msg = op.message
            Id = msg.id
            R = msg.to or to
            D = msg._from
            Proses_message = msg.text
            if Proses_message == "Active" or Proses_message == "active":
                if D in Owner or D in meM:
                    wait["bot"] = True
                    me.sendMessage(R,"Bot active")
                    me.sendMessage(R,"Already Ok "+me.getContact(D).displayName)
                    Run_Xx()
                    
            if Proses_message == "Non active" or Proses_message == "non active":
                print ("NOTIF BOT NON ACTIVE")
                if D in Owner or D in meM:
                    wait["bot"] = False
                    me.sendMessage(R,"Bot Non Active")
                    me.sendMessage(R,"Ok I'am Turn down "+me.getContact(D).displayName)
                
        if op.type == 25 or op.type == 26:
          if wait["bot"] == True:
            msg = op.message
            text = msg.text
            Id = msg.id
            R = msg.to or to
            D = msg._from
            Gr = op.param1
            OperWaitData = wait["text"].title()
            if wait["key"] == False:
                 OperWaitData = ''
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if D != me.profile.mid:
                        to = D
                    else:
                        to = R
                elif msg.toType == 1:
                    to = R
                elif msg.toType == 2:
                    to = R
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        WaitData = SqL_R(text)
                        if WaitData == Abouts["1"]:
                          if D in Owner or D in meM:
                            Res= extras+Stiles+Abouts["0"]+"\n"
                            Res+= Stiles+"1. "+OperWaitData+Abouts["1"]+"\n"
                            Res+= Stiles+"2. "+OperWaitData+Abouts["2"]+"\n"
                            Res+= Stiles+"3. "+OperWaitData+Abouts["3"]+"\n"
                            Res+= Stiles+"4. "+OperWaitData+Abouts["4"]+"\n"
                            Res+= Stiles+"5. "+OperWaitData+Abouts["5"]+"\n"
                            Res+= Stiles+"6. "+OperWaitData+Abouts["6"]+"\n"
                            Res+= Stiles+"7. "+OperWaitData+Abouts["7"]+"\n"
                            Res+= Stiles+"8. "+OperWaitData+Abouts["8"]+" *porn\n"
                            Res+= Stiles+"9. "+OperWaitData+Abouts["9"]+" *judul\n"
                            Res+= Stiles+"10. "+OperWaitData+Abouts["10"]+" *tags\n"
                            Res+= Stiles+"11. "+OperWaitData+Abouts["11"]+"\n"
                            Res+= Stiles+"12. "+OperWaitData+Abouts["12"]+" *txt/txt/txt\n"
                            Res+= Stiles+"13. "+OperWaitData+Abouts["13"]+" *text\n"
                            Res+= Stiles+"14. "+OperWaitData+Abouts["14"]+"\n"
                            Res+= Stiles+"15. "+OperWaitData+Abouts["15"]+"\n"
                            Res+= Stiles+"16. "+OperWaitData+Abouts["16"]+"\n"
                            Res+= Stiles+"17. "+OperWaitData+Abouts["17"]+"\n"
                            Res+= Stiles+"18. "+OperWaitData+Abouts["18"]+"\n"
                            Res+= Stiles+"19. "+OperWaitData+Abouts["19"]+" *tags\n"
                            Res+= Stiles+"20. "+OperWaitData+Abouts["20"]+" *tags\n"
                            Res+= Stiles+"21. "+OperWaitData+Abouts["21"]+" *tags\n"
                            Res+= Stiles+"22. "+OperWaitData+Abouts["22"]+" *tags\n"
                            Res+= Stiles+"23. "+OperWaitData+Abouts["23"]+" *tags\n"
                            Res+= Stiles+"24. "+OperWaitData+Abouts["24"]+" *tags\n"
                            Res+= Stiles+"25. "+OperWaitData+Abouts["25"]+" *text\n"
                            Res+= Stiles+"26. "+OperWaitData+Abouts["26"]+" *01-02-1995\n"
                            Res+= Stiles+"27. "+OperWaitData+Abouts["27"]+" *id ig\n"
                            Res+= Stiles+"28. "+OperWaitData+Abouts["28"]+" *id smule\n"
                            Res+= Stiles+"29. "+OperWaitData+Abouts["29"]+"\n"
                            Res+= Stiles+"30. "+OperWaitData+Abouts["30"]+" *text\n"
                            Res+= Stiles+"31. "+OperWaitData+Abouts["31"]+" *text\n"
                            Res+= Stiles+"32. "+OperWaitData+Abouts["32"]+"\n"
                            Res+= Stiles+"33. "+OperWaitData+Abouts["33"]+" *text\n"
                            Res+= Stiles+"34. "+OperWaitData+Abouts["34"]+"\n"
                            Res+= Stiles+"35. "+OperWaitData+Abouts["35"]+"\n"
                            Res+= Stiles+"36. "+OperWaitData+Abouts["36"]+"\n"
                            Res+= Stiles+"37. "+OperWaitData+Abouts["37"]+"\n"
                            Res+= Stiles+"38. "+OperWaitData+Abouts["38"]+"\n"
                            Res+= Stiles+"39. "+OperWaitData+Abouts["39"]+"\n"
                            Res+= Stiles+"40. "+OperWaitData+Abouts["40"]+"\n"
                            Res+= Stiles+"41. "+OperWaitData+Abouts["41"]+"\n"
                            Res+= Stiles+"42. "+OperWaitData+Abouts["42"]+"\n"
                            Res+= Stiles+"43. "+OperWaitData+Abouts["43"]+"\n"
                            Res+= Stiles+"44. "+OperWaitData+Abouts["44"]+"\n"
                            Res+= Stiles+"45. "+OperWaitData+Abouts["45"]+"\n"
                            Res+= Stiles+"46. "+OperWaitData+Abouts["46"]+"\n"
                            Res+= Stiles+"47. "+OperWaitData+Abouts["47"]+"\n"
                            Res+= Stiles+"48. "+OperWaitData+Abouts["48"]+"\n"
                            Res+= Stiles+"49. "+OperWaitData+Abouts["49"]+"\n"
                            Res+= Stiles+"50. "+OperWaitData+Abouts["50"]+"\n"
                            Res+= Stiles+"51. "+OperWaitData+Abouts["51"]+"\n"
                            Res+= Stiles+"52. "+OperWaitData+Abouts["52"]+"\n"
                            Res+= Stiles+"53. "+OperWaitData+Abouts["53"]+"\n"
                            Res+= Stiles+"54. "+OperWaitData+Abouts["54"]+"\n"
                            Res+= Stiles+"55. "+OperWaitData+Abouts["55"]+"\n"
                            Res+= Stiles+"56. "+OperWaitData+Abouts["56"]+"\n"
                            Res+= Stiles+"57. "+OperWaitData+Abouts["57"]+"\n"
                            Res+= Stiles+"58. "+OperWaitData+Abouts["58"]+"\n"
                            Res+= Stiles+"59. "+OperWaitData+Abouts["59"]+"\n"
                            Res+= Stiles+"60. "+OperWaitData+Abouts["60"]+"\n"
                            Res+= Stiles+"61. "+OperWaitData+Abouts["61"]+"\n"
                            Res+= Stiles+"62. "+OperWaitData+Abouts["62"]+"\n"
                            Res+= Stiles+"63. "+OperWaitData+Abouts["63"]+"\n"
                            Res+= Stiles+"64. "+OperWaitData+Abouts["64"]+"\n"
                            Res+= Stiles+"65. "+OperWaitData+Abouts["65"]+"\n"
                            Res+= Stiles+"66. "+OperWaitData+Abouts["66"]+"\n"
                            Res+= Stiles+"67. "+OperWaitData+Abouts["67"]+" [invite bot]\n"
                            Res+= Stiles+"68. "+OperWaitData+Abouts["68"]+" [bot leave]\n"
                            Res+= Stiles+"69. "+OperWaitData+Abouts["69"]+"\n"
                            Res+= Stiles+"70. "+OperWaitData+Abouts["70"]+"\n"
                            Res+= Stiles+"71. "+OperWaitData+Abouts["76"]+"\n"
                            Res+= Stiles+"72. "+OperWaitData+Abouts["71"]+" [delete blacklist]\n"
                            Res+= Stiles+"73. "+OperWaitData+Abouts["72"]+"\n"
                            Res+= Stiles+"74. "+OperWaitData+Abouts["73"]+" @ [self bot kick target]\n"
                            Res+= Stiles+"75. "+OperWaitData+Abouts["74"]+" @ [bot kick target]\n"
                            Res+= Stiles+"76. "+OperWaitData+Abouts["75"]+"\n"
                            Res+= Stiles+"77. "+OperWaitData+Abouts["77"]+" *tags\n"
                            Res+= Stiles+"78. "+OperWaitData+Abouts["78"]+" *tags\n"
                            Res+= Stiles+"79. "+OperWaitData+Abouts["79"]+"\n"
                            Res+= Stiles+"80. "+OperWaitData+Abouts["80"]+"\n"
                            Res+= Stiles+"81. "+OperWaitData+Abouts["81"]+"\n"
                            Res+= Stiles+"82. "+OperWaitData+Abouts["82"]+"\n"
                            Res+= Stiles+"_____CHECK BOT______\n"
                            if wait["Add"] == True: Res+= Stiles+" autoadd->『on』\n"
                            else: Res+= Stiles+" autoadd->『off』\n"
                            if wait["Shared"] == True: Res+= Stiles+" shared->『on』\n"
                            else: Res+= Stiles+" shared->『off』\n"
                            if wait["Join"] == True: Res+= Stiles+" autojoin->『on』\n"
                            else: Res+= Stiles+" autojoin->『off』\n"
                            if wait["Read"] == True: Res+= Stiles+" autoread->『on』\n"
                            else: Res+= Stiles+" autoread->『off』\n"
                            if wait["Unsend"] == True: Res+= Stiles+" unsend->『on』\n"
                            else: Res+= Stiles+" unsend->『off』\n"
                            if wait["Wc"] == True: Res+= Stiles+" welcome->『on』\n"
                            else: Res+= Stiles+" welcome->『off』\n"
                            if wait["Respon"] == True: Res+= Stiles+" respon->『on』\n"
                            else: Res+= Stiles+" respon->『off』\n"
                            Protection = ""
                            a = 0
                            gid = wait["PROTECT"]
                            for group in gid:
                                a = a + 1
                                end = '\n'
                                pli = Stiles + str(a) + ". " +me.getGroup(group).name
                            Res += Stiles+"━━━━━p̲̅r̲̅o̲̅t̲̅e̲̅c̲̅t̲̅ g̲̅r̲̅o̲̅u̲̅p̲̅━━━━━━"+Protection+"\n"+Stiles+"━━━━ %s DI PROTECT ━━━━\n" %(str(len(wait["PROTECT"])))
                            Res += Stiles+"____________________\n"
                            Res += Stiles+"______SelfName______\n"+Stiles+meProfile.displayName+"\n"
                            me.sendContact(R,apikey_com)
                            me.sendMessage(R, str(Res)+Stiles+"Contact Owner\n"+Stiles+" http://line.me/ti/p/~hanavy1992")
                        if WaitData == Abouts["2"]:
                          if D in Owner or D in meM:
                            try:
                                me.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot1.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot2.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot3.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot4.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot5.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot6.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot7.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot8.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                Java_script.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                Java_script2.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                Musik(R)
                                RunTheRun(apikey_com, D, "_______RESULT______\n")
                            except:Musik(R)
                        if WaitData == Abouts["3"]:
                          if D in Owner or D in meM:
                            me.reissueUserTicket()
                            My_Id = me.profile.displayName + "\nMy id Line: http://line.me/ti/p/" + me.getUserTicket().id
                            me.sendMessage(R,My_Id)
                        if WaitData == Abouts["4"]:
                          if D in meM:
                            me.leaveGroup(R)
                        if WaitData == Abouts["5"]:
                          if D in Owner or D in meM:
                            h = me.getContact(D)
                            cu = me.getProfileCoverURL(D)          
                            path = str(cu)
                            me.sendImageWithURL(R, path)
                        if WaitData == Abouts["6"]:
                          if D in Owner or D in meM:
                            result = requests.get("http://jadwalnonton.com/")
                            data = BeautifulSoup(result.content, 'html5lib')
                            hasil = "_______CINEMA______\nType : Movie List Today\n"
                            no = 1
                            for dzin in data.findAll('div', attrs={'class':'col-xs-6 moside'}):
                                hasil += "\n\n{}. {}".format(str(no), str(dzin.find('h2').text))
                                hasil += "\n     Link : {}".format(str(dzin.find('a')['href']))
                                no = (no+1)
                            me.sendMessage(R, str(hasil))
                        if WaitData == Abouts["7"]:
                          if D in Owner or D in meM:
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(wait["userAgent"])
                                r = web.get('http://api-1cak.herokuapp.com/random')
                                data = r.text
                                data = json.loads(data)
                                img = data["img"]
                                me.sendMessage(R,"━═| Daftar cakcak |═━\n━═| Title: %s\n━═| Link: %s\n━═| Id: %s\n━═| Votes: %s\n━═| NSFW: %s\n━═| [ Finish ] |═━" %(str(data["title"].replace('FACEBOOK Comments', ' ')), str(data["url"]), str(data["id"]), str(data["votes"]), str(data["nsfw"])))
                        if WaitData.startswith(Abouts["8"]):
                          if D in Owner or D in meM:
                            separate = text.split(" ")
                            kata = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(wait["userAgent"])
                                try:
                                    r = web.get("https://api.redtube.com/?data=redtube.Videos.searchVideos&output=json&search={}".format(urllib.parse.quote(kata)))
                                    data = r.text
                                    data = json.loads(data)
                                    ret_ = "━═Bokep ini mah"
                                    no = 1
                                    anu = data["videos"]
                                    if len(anu) >= 20:
                                        for s in range(20):
                                            hmm = anu[s]
                                            title = hmm['video']['title']
                                            duration = hmm['video']['duration']
                                            views = hmm['video']['views']
                                            link = hmm['video']['embed_url']
                                            ret_ += "\n━═ {}. \nTitle ━═ {}\nDurasi ━═ {}\nViews ━═ {}\nLink ━═ {}".format(str(no), str(title), str(duration), str(views), str(link))
                                            no += 1
                                    else:
                                        for s in anu:
                                            hmm = s
                                            title = hmm['video']['title']
                                            duration = hmm['video']['duration']
                                            views = hmm['video']['views']
                                            link = hmm['video']['embed_url']
                                            ret_ += "\n━═ {}. \nTitle ━═ {}\nDurasi ━═ {}\nViews ━═ {}\nLink ━═ {}".format(str(no), str(title), str(duration), str(views), str(link))
                                            no += 1
                                    me.sendMessage(R, str(ret_))
                                except:
                                    me.sendMessage(R, "Tidak ditemukan")
                        if WaitData.startswith(Abouts["9"]):
                          if D in Owner or D in meM:
                            sep = text.split(" ")
                            title = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(wait["userAgent"])
                                r = web.get("http://www.omdbapi.com/?t="+title+"&y=&plot=full&apikey=4bdd1d70")
                                data=r.text
                                data=json.loads(data)
                                hasil = "╭━━═════[ Hasil pencarian film]"
                                hasil += "\nInformasi ━═| " +str(data["Title"])+ " (" +str(data["Year"])+ ")"
                                hasil += "\nPlot ━═| " +str(data["Plot"])
                                hasil += "\nDirector ━═| " +str(data["Director"])
                                hasil += "\nActors ━═| " +str(data["Actors"])
                                hasil += "\nRelease ━═| " +str(data["Released"])
                                hasil += "\nGenre ━═| " +str(data["Genre"])
                                hasil += "\nTimer ━═| " +str(data["Runtime"])
                                img = data["Poster"]
                                me.sendImageWithURL(R,img)
                                me.sendMessage(R,hasil)
                        if WaitData.startswith(Abouts["10"]):
                          if D in Owner or D in meM:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]                
                            mmid = me.getContact(key1)
                            me.findAndAddContactsByMid(key1)
                            me.sendMessage(R, "teman di tambahkan")
                        if WaitData == Abouts["11"]:
                          if D in meM:
                            me.sendMessage(R, "Selesai.!!")
                            Run_Xp()
                        if WaitData.startswith(Abouts["12"]):
                          if D in Owner or D in meM:
                            separate = text.split(" ")
                            teks = text.replace(separate[0] + " ","")
                            txt = teks.split("/")
                            bag1 = txt[0]
                            bag2 = txt[1]
                            bag3 = txt[2]
                            angka = ["1","2","3","4","5"]
                            latar = random.choice(angka)
                            nomor = ["1","2","3","4"]
                            background = random.choice(nomor)
                            url = "https://ari-api.herokuapp.com/retro?bg="+latar+"&txt="+background+"&text1="+bag1+"&text2="+bag2+"&text3="+bag3
                            me.sendImageWithURL(R, url)
                        if WaitData.startswith(Abouts["13"]):
                          if D in Owner or D in meM:
                            separate = text.split(" ")
                            teks = text.replace(separate[0] + " ","")
                            url = "https://ari-api.herokuapp.com/led?text="+teks+"&sign=PB"
                            me.sendImageWithURL(R, url)
                        if WaitData == Abouts["14"]:
                          if D in Owner or D in meM:
                            timeNow = time.time()
                            runtime = timeNow - botStart
                            runtime = format_timespan(runtime)
                            me.sendMessage(R, "━━━━━╦RUNTIME BOTS╦━━━━━\n ┣━╦[ {}".format(str(runtime)))
                        if WaitData == Abouts["15"]:
                          if D in Owner or D in meM:
                            start = time.time()
                            me.sendMessage(R, "Menghitung Kecepatan Respon Bot...")
                            elapsed_time = time.time() - start
                            me.sendMessage(R,"↓[Kecepatan Respon Bot]↓\n"+format(str(elapsed_time)))
                        if WaitData == Abouts["16"]:
                          if D in Owner or D in meM:
                            h = me.getContact(D)
                            me.sendMessage(R,h.mid)
                        if WaitData == Abouts["17"]:
                          if D in Owner or D in meM:
                            contact = me.getContact(D)
                            cover = me.getProfileCoverURL(D)
                            result = "╔══[ Details Profile ]"
                            result += "\n╠ Display Name : {}".format(contact.displayName)
                            result += "\n╠ Mid : {}".format(contact.mid)
                            result += "\n╠ Status Message : {}".format(contact.statusMessage)
                            result += "\n╠ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            result += "\n╠ Cover : {}".format(str(cover))
                            result += "\n╚══[ Finish ]"
                            me.sendImageWithURL(R, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            me.sendImageWithURL(R, str(cover))
                            me.sendMessage(R, str(result))
                        if WaitData == Abouts["18"]:
                          if D in Owner or D in meM:
                            h = me.getContact(D)
                            me.sendVideoWithURL(R,"http://dl.profile.line-cdn.net/" + h.pictureStatus + "/vp")
                        if WaitData.startswith(Abouts["19"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                ret_ = ""
                                for ls in lists:
                                    ret_ += "{}".format(str(ls))
                                me.sendMessage(R, str(ret_))
                        if WaitData.startswith(Abouts["20"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.me.naver.jp/" + me.getContact(ls).pictureStatus
                                    me.sendImageWithURL(R, str(path))
                        if WaitData.startswith(Abouts["21"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.me.naver.jp/" + me.getContact(ls).pictureStatus + "/vp"
                                    me.sendVideoWithURL(R, str(path))
                        if WaitData.startswith(Abouts["22"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = me.getContact(ls)
                                    me.sendMessage(R, "Namanya\n{}".format(str(contact.displayName)))
                        if WaitData.startswith(Abouts["23"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = me.getContact(ls)
                                    me.sendMessage(R, "Status kontak\n\n{}".format(str(contact.statusMessage)))
                        if WaitData.startswith(Abouts["24"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = me.getContact(ls)
                                    mi_d = contact.mid
                                    me.sendContact(R, mi_d)
                        if WaitData.startswith(Abouts["25"]):
                          if D in Owner or D in meM:
                            me.sendMessage(R, "Waiting...")
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            params = {"search_query": search}
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(wait["userAgent"])
                                r = web.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╭━━━━━[ Youtube link di tampilkan ]━"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n┣[ {} ]".format(str(data["title"]))
                                    ret_ += "\n┣━ https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n╰━━━━━━━━[ Total {} link]━━━━━".format(len(datas))
                                me.sendMessage(R, str(ret_))
                        if WaitData.startswith(Abouts["26"]):
                          if D in Owner or D in meM:
                            try:
                                sep = msg.text.split(" ")
                                tanggal = msg.text.replace(sep[0] + " ","")
                                r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                data=r.text
                                data=json.loads(data)
                                ret_ = "╭━━━━════[Tanggal,Lahir]"
                                ret_ += "\n┣═Tanggal lahir : {}".format(str(data["data"]["lahir"]))
                                ret_ += "\n┣═Umur : {}".format(str(data["data"]["usia"]))
                                ret_ += "\n┣═Tanggal ultah : {}".format(str(data["data"]["ultah"]))
                                ret_ += "\n┣═Zodiak : {}".format(str(data["data"]["zodiak"]))
                                ret_ += "\n╰━━═════[==================]"
                                me.sendMessage(R, str(ret_))
                            except Exception as error:
                                logError(error)
                        if WaitData.startswith(Abouts["27"]):
                          if D in Owner or D in meM:
                            sep = text.split(" ")
                            instagram = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(wait["userAgent"])
                                html = web.get("https://www.instagram.com/" + instagram + "/")
                                soup = BeautifulSoup(html.text, 'html5lib')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://instagram.com/" + instagram
                                me.sendImageWithURL(R, text1[0])
                                me.sendMessage(R, user + user1 + followers + following + post + link)
                                print("[Notif] Search Instagram Sucess")
                        if WaitData.startswith(Abouts["28"]):
                          if D in Owner or D in meM:
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            smule = "https://www.smule.com/"+ key
                            me.sendMessage(R, "ini id smulenya plak\n" + smule)
                        if WaitData == Abouts["29"]:
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                group = me.getGroup(R)
                                members = [mem.mid for mem in group.members]
                                me.acquireGroupCallRoute(R)
                                me.inviteIntoGroupCall(R, contactIds=members)
                                me.sendMessage(R, "Berhasil")
                        if WaitData.startswith(Abouts["30"]):
                          if D in Owner or D in meM:
                            sep = text.split(" ")
                            say = text.replace(sep[0] + " ","")
                            lang = 'id'
                            tts = gTTS(text=say, lang=lang)
                            tts.save("hasil.mp3")
                            me.sendAudio(R,"hasil.mp3")
                        if WaitData.startswith(Abouts["31"]):
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                X = me.getGroup(R)
                                sep = msg.text.split(" ")
                                X.name = msg.text.replace(sep[0] + " ","")
                                me.updateGroup(X)
                        if WaitData == Abouts["32"]:
                          if D in Owner or D in meM:
                            me.removeAllMessages(op.param2)
                            me.sendMessage(R, "Chat deleted")
                        if WaitData.startswith(Abouts["33"]):
                          if D in Owner or D in meM:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            groups = me.groups
                            for group in groups:
                                sendMessageWithFooter(group, "╭━━━━━╦BroadCast by Self╦━━━━━╮\n{}".format(str(txt))+"\nContact Owner:\nhttp://line.me/ti/p/~hanavy1992")
                            me.sendMessage(R, "Berhasil broadcast ke {} group".format(str(len(groups))))
                        if WaitData == Abouts["34"]:
                          if D in Owner or D in meM:
                            groups = me.groups
                            ret_ = "╭━━━━━══[ Group List ]══━━━━━╮"
                            no = 0 + 1
                            for gid in groups:
                                group = me.getGroup(gid)
                                ret_ += "\n┣═ {}. {} ┣═Member: {}".format(str(no), str(group.name), str(len(group.members)))
                                no += 1
                            ret_ += "\n╰━━━━━══[ Total {} Groups ]════━━━━━".format(str(len(groups)))
                            me.sendMessage(R, str(ret_))
                        if WaitData == Abouts["35"]:
                          if D in Owner or D in meM:
                            contactlist = me.getAllContactIds()
                            kontak = me.getContacts(contactlist)
                            num=1
                            msgs="╭━━━━━══[ Friend List ]══━━━━━╮"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n━━━━━══[ Friend Result ]══━━━━━\nTotal : %i" % len(kontak)
                            me.sendMessage(R, msgs)
                        if WaitData == Abouts["36"]:
                          if D in Owner or D in meM:
                            blockedlist = me.getBlockedContactIds()
                            kontak = me.getContacts(blockedlist)
                            num=1
                            msgs="╭━━━━━══[ Friend Block ]══━━━━━╮"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n━━━━━══[ Block Result ]══━━━━━\nBlock Total : %i" % len(kontak)
                            me.sendMessage(R, msgs)
                        if WaitData == Abouts["37"]:
                          if D in Owner or D in meM:
                            me.sendMessage(R, "━━━━══[Pembuat Grup]══━━━━")
                            group = me.getGroup(R)
                            GS = group.creator.mid
                            me.sendContact(R, GS)
                            me.sendMessage(R, "━━━━══━━╩━━══━━━━")
                        if WaitData == Abouts["38"]:
                          if D in Owner or D in meM:
                            if D in meM:
                                if msg.toType == 2:
                                    group = me.getGroup(R)
                                    ret_ = "╭━━━══[ Member List ]"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n┣═ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╰━━━══[ Total {} member]".format(str(len(group.members)))
                                    me.sendMessage(R, str(ret_))
                        if WaitData == Abouts["39"]:
                          if D in Owner or D in meM:
                            if D in meM:
                                if msg.toType == 2:
                                    group = me.getGroup(R)
                                    ret_ = "╭━━━══[ Pending List ]"
                                    no = 0 + 1
                                    if group.invitee is None or group.invitee == []:
                                        me.sendMessage(R, "Tidak ada pendingan")
                                        return
                                    else:
                                        for pen in group.invitee:
                                            ret_ += "\n┣═ {}. {}".format(str(no), str(pen.displayName))
                                            no += 1
                                        ret_ += "\n╰━━━══[ Total {} tertunda]".format(str(len(group.invitee)))
                                        me.sendMessage(R, str(ret_))
                        if WaitData == Abouts["40"]:
                          if D in Owner or D in meM:
                            if D in meM:
                                group = me.getGroup(R)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Closed"
                                    gTicket = "Qr tidak tersedia karna di tutup"
                                else:
                                    gQr = "Open"
                                    gTicket = "https://me.me/R/ti/g/{}".format(str(me.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "╭━━━━══[ Group Info ]"
                                ret_ += "\n┣═Nama Group : {}".format(str(group.name))
                                ret_ += "\n┣═ID Group : {}".format(group.id)
                                ret_ += "\n┣═Pembuat : {}".format(str(gCreator))
                                ret_ += "\n┣═Jumlah Member : {}".format(str(len(group.members)))
                                ret_ += "\n┣═Jumlah Pending : {}".format(gPending)
                                ret_ += "\n┣═━━━Kode Qr/Link━━━═"
                                ret_ += "\n┣═Group Ticket : {}".format(gTicket)
                                ret_ += "\n┣═Group Qr : {}".format(gQr)
                                ret_ += "\n╰━━━━══[ END ]"
                                me.sendImageWithURL(R, path)
                                me.sendMessage(R, str(ret_))
                        if WaitData == Abouts["41"]:
                          if D in Owner or D in meM:
                            group = me.getGroup(R)
                            path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            me.sendImageWithURL(R, path)
                        if WaitData == Abouts["42"]:
                          if D in Owner or D in meM:
                            gid = me.getGroup(R)
                            me.sendMessage(R, "Name group\n" + gid.name)
                        if WaitData == Abouts["43"]:
                          if D in Owner or D in meM:
                            gid = me.getGroup(R)
                            me.sendMessage(R,gid.id)
                        if WaitData == Abouts["44"]:
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                group = me.getGroup(R)
                                if group.preventedJoinByTicket == False:
                                    ticket = me.reissueGroupTicket(R)
                                    me.sendMessage(R, "https://line.me/R/ti/g/{}".format(str(ticket)))
                                else:
                                    group.preventedJoinByTicket = False
                                    me.updateGroup(group)
                                    me.sendMessage(R, "https://line.me/R/ti/g/{}".format(str(ticket)))
                        if WaitData == Abouts["45"]:
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                group = me.getGroup(R)
                                if group.preventedJoinByTicket == False:
                                    me.sendMessage(R, "Sudah terbuka")
                                else:
                                    group.preventedJoinByTicket = False
                                    me.updateGroup(group)
                                    me.sendMessage(R, "Berhasil membuka Qr")
                        if WaitData == Abouts["46"]:
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                group = me.getGroup(R)
                                if group.preventedJoinByTicket == True:
                                    me.sendMessage(R, "Sudah tertutup")
                                else:
                                    group.preventedJoinByTicket = True
                                    me.updateGroup(group)
                                    me.sendMessage(R, "Berhasil menutup Qr")
                        if WaitData == Abouts["47"]:
                          if D in Owner or D in meM:
                            wait["Add"] = True
                            me.sendMessage(R, "Already on")
                        if WaitData == Abouts["48"]:
                          if D in Owner or D in meM:
                            wait["Add"] = False
                            me.sendMessage(R, "Already ff")
                        if WaitData == Abouts["49"]:
                          if D in Owner or D in meM:
                            wait["Join"] = True
                            me.sendMessage(R, "Already on")
                        if WaitData == Abouts["50"]:
                          if D in Owner or D in meM:
                            wait["Join"] = False
                            me.sendMessage(R, "Already off")
                        if WaitData == Abouts["51"]:
                          if D in Owner or D in meM:
                            wait["Read"] = True
                            me.sendMessage(R, "Already on")
                        if WaitData == Abouts["52"]:
                          if D in Owner or D in meM:
                            wait["Read"] = False
                            me.sendMessage(R, "Already off")
                        if WaitData == Abouts["53"]:
                          if D in Owner or D in meM:
                            wait["Unsend"] = True
                            me.sendMessage(R, "Already on")
                        if WaitData == Abouts["54"]:
                          if D in Owner or D in meM:
                            wait["Unsend"] = False
                            me.sendMessage(R, "Already off")
                        if WaitData == Abouts["55"]:
                          if D in Owner or D in meM:
                            wait["Wc"] = True
                            me.sendMessage(R, "Already on")
                        if WaitData == Abouts["56"]:
                          if D in Owner or D in meM:
                            wait["Wc"] = False
                            me.sendMessage(R, "Already off")
                        if WaitData == Abouts["57"]:
                          if D in Owner or D in meM:
                            wait["Shared"] = True
                            me.sendMessage(R, "Already on")
                        if WaitData == Abouts["58"]:
                          if D in Owner or D in meM:
                            wait["Shared"] = False
                            me.sendMessage(R, "Already off")
                        if WaitData == Abouts["59"]:
                          if D in Owner or D in meM:
                            wait["Respon"] = True
                            me.sendMessage(R, "Already on")
                        if WaitData == Abouts["60"]:
                          if D in Owner or D in meM:
                            wait["Respon"] = False
                            me.sendMessage(R, "Already off")
                        if WaitData == Abouts["61"]:
                          groups = me.getGroup(msg.to)
                          if D in Owner or D in meM:
                            try:
                              del cctv['point'][msg.to]
                              del cctv['sidermem'][msg.to]
                              del cctv['cyduk'][msg.to]
                            except:
                              pass
                            cctv['point'][msg.to] = msg.id
                            cctv['sidermem'][msg.to] = ""
                            cctv['cyduk'][msg.to]=True
                            wait["Sider"] = True
                            me.sendMessage(msg.to,"Sider Diaktifkan Untuk Group\n"+"→"+groups.name+"←")
                            #me.sendMessage(R, "Sider Di Aktifkan")
                        if WaitData == Abouts["62"]:
                          groups = me.getGroup(msg.to)
                          if D in Owner or D in meM:
                            if msg.to in cctv['point']:
                              cctv['cyduk'][msg.to]=False
                              wait["Sider"] = False
                              me.sendMessage(msg.to, "Sider Dimatikan Untuk Group\n"+"→"+groups.name+"←")
                              me.sendMessage(msg.to, "Daftar Mahluk Yang Sudah Terlihat\n"+cctv['sidermem'][msg.to])
                            else:
                              me.sendMessage(msg.to, "Woyyy\nBelom Di Set")
                        if WaitData == Abouts["63"]:
                         if D in Owner or D in meM:
                               group = me.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7, jml = [], [], [], [],[], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                        if WaitData == Abouts["64"]:
                          MIDBOT = [BotRanger,BotRanger2,BotRanger3,BotRanger4,BotRanger5,BotRanger6,BotRanger7,BotRanger8,Java_scriptRanger,Java_script2Ranger]
                          if D in meM:
                            try:
                                wait["Shared"] = True
                                wait["Add"] = True
                                wait["Join"] = True
                                wait["Wc"] = True
                                wait["Read"] = True
                                wait["Unsend"] = True
                                me.findAndAddContactsByMid(R,MIDBOT)
                                bot1.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot2.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot3.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot4.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot5.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot6.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot7.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot8.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                Java_script.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                Java_script2.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                me.sendMessage(R,"SETTING ALL IN ONLINE")
                            except:me.sendMessage(R,"SETTING ALL IN ONLINE")
                        if WaitData == Abouts["65"]:
                          MIDBOT = [BotRanger,BotRanger2,BotRanger3,BotRanger4,BotRanger5,BotRanger6,BotRanger7,BotRanger8,Java_scriptRanger,Java_script2Ranger]
                          if D in meM:
                            try:
                                wait["Shared"] = False
                                wait["Add"] = False
                                wait["Join"] = False
                                wait["Wc"] = False
                                wait["Read"] = False
                                wait["Unsend"] = False
                                me.findAndAddContactsByMid(R,MIDBOT)
                                bot1.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot2.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot3.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot4.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot5.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot6.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot7.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                bot8.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                Java_script.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                Java_script2.findAndAddContactsByMid("ubaba90be636d918cab5509685cef5c23")
                                me.sendMessage(R,"SETTING ALL IN OFFLINE")
                            except:me.sendMessage(R,"SETTING ALL IN OFFLINE")
                        if WaitData == Abouts["66"]:
                          if D in Owner or D in meM:
                            RunTheRun(R, D, "_______RESULT______\n")
                        if WaitData == Abouts["67"]:
                          if D in meM:
                              PASUKAN = [BotRanger,BotRanger2,BotRanger3,BotRanger4,BotRanger5,BotRanger6,BotRanger7,BotRanger8,Java_scriptRanger,Java_script2Ranger]
                              PASUKANANTIJS = [Java_scriptRanger,Java_script2Ranger]
                              try:
                                 me.inviteIntoGroup(R,PASUKAN)
                                 bot1.acceptGroupInvitation(R)
                                 bot2.acceptGroupInvitation(R)
                                 bot3.acceptGroupInvitation(R)
                                 bot4.acceptGroupInvitation(R)
                                 bot5.acceptGroupInvitation(R)
                                 bot6.acceptGroupInvitation(R)
                                 bot7.acceptGroupInvitation(R)
                                 bot8.acceptGroupInvitation(R)
                              except:
                                 P = me.getGroup(R)
                                 P.preventedJoinByTicket = False
                                 invsend = 0 #INI PERLU JIKA PAKAI COMMAND
                                 Targ = me.reissueGroupTicket(R)
                                 bot1.acceptGroupInvitationByTicket(R,Targ)
                                 bot2.acceptGroupInvitationByTicket(R,Targ)
                                 bot3.acceptGroupInvitationByTicket(R,Targ)
                                 bot4.acceptGroupInvitationByTicket(R,Targ)
                                 bot5.acceptGroupInvitationByTicket(R,Targ)
                                 bot6.acceptGroupInvitationByTicket(R,Targ)
                                 bot7.acceptGroupInvitationByTicket(R,Targ)
                                 bot8.acceptGroupInvitationByTicket(R,Targ)
                                 bot1.findAndAddContactsByMid(Java_scriptRanger)
                                 bot1.findAndAddContactsByMid(Java_script2Ranger)
                                 bot1.inviteIntoGroup(R,[Java_scriptRanger])
                                 bot1.inviteIntoGroup(R,[Java_script2Ranger])
                        if WaitData == Abouts["68"]:
                          if D in meM:
                            try:
                              random.choice(KACOP).cancelGroupInvitation(R,[Java_scriptRanger])
                              random.choice(KACOP).cancelGroupInvitation(R,[Java_script2Ranger])
                              bot8.leaveGroup(R)
                              bot7.leaveGroup(R)
                              bot6.leaveGroup(R)
                              bot5.leaveGroup(R)
                              bot4.leaveGroup(R)
                              bot3.leaveGroup(R)
                              bot2.leaveGroup(R)
                              bot1.leaveGroup(R)
                            except:
                              bot8.leaveGroup(R)
                              bot7.leaveGroup(R)
                              bot6.leaveGroup(R)
                              bot5.leaveGroup(R)
                              bot4.leaveGroup(R)
                              bot3.leaveGroup(R)
                              bot2.leaveGroup(R)
                              bot1.leaveGroup(R)
                        if WaitData == Abouts["69"]:
                          if D in meM:
                              if R in wait["PROTECT"]:
                                  me.sendMessage(R,"Sudah on")
                                  bot1.sendMessage(R,"Sudah on")
                                  bot2.sendMessage(R,"Sudah on")
                                  bot3.sendMessage(R,"Sudah on")
                                  bot4.sendMessage(R,"Sudah on")
                                  bot5.sendMessage(R,"Sudah on")
                                  bot6.sendMessage(R,"Sudah on")
                                  bot7.sendMessage(R,"Sudah on")
                                  bot8.sendMessage(R,"Sudah on")
                              else:
                                  wait["PROTECT"][R] = True
                                  me.sendMessage(R,"Already on..")
                                  bot1.sendMessage(R,"Already on..")
                                  bot2.sendMessage(R,"Already on..")
                                  bot3.sendMessage(R,"Already on..")
                                  bot4.sendMessage(R,"Already on..")
                                  bot5.sendMessage(R,"Already on..")
                                  bot6.sendMessage(R,"Already on..")
                                  bot7.sendMessage(R,"Already on..")
                                  bot8.sendMessage(R,"Already on..")
                        if WaitData == Abouts["70"]:
                          if D in meM:
                              if R in wait["PROTECT"]:
                                  me.sendMessage(R,"Already off")
                                  bot1.sendMessage(R,"Already off")
                                  bot2.sendMessage(R,"Already off")
                                  bot3.sendMessage(R,"Already off")
                                  bot4.sendMessage(R,"Already off")
                                  bot5.sendMessage(R,"Already off")
                                  bot6.sendMessage(R,"Already off")
                                  bot7.sendMessage(R,"Already off")
                                  bot8.sendMessage(R,"Already off")
                                  del wait["PROTECT"][R]
                              else:
                                  me.sendMessage(R,"Belum di protect")
                                  bot1.sendMessage(R,"ok siap")
                                  bot2.sendMessage(R,"ok siap")
                                  bot3.sendMessage(R,"ok siap")
                                  bot4.sendMessage(R,"ok siap")
                                  bot5.sendMessage(R,"ok siap")
                                  bot6.sendMessage(R,"ok siap")
                                  bot7.sendMessage(R,"ok siap")
                                  bot8.sendMessage(R,"ok siap")
                        if WaitData == Abouts["76"]:
                            if D in Owner or D in meM:
                                thanks = ""
                                a = 0
                                Ban = wait["blacklist"]
                                for Crott in Ban:
                                    a = a + 1
                                    end = '\n'
                                    thanks += "\n┣|" + str(a) + ". " +me.getContact(Crott).displayName
                                me.sendMessage(R, "━━━━━━━╦One Piece Team╦━━━━━━━\n━━━━━daftar blacklist━━━━━━"+thanks+"\n┣━━━━━━★ONE PIECE TEAM★━━━━━━━\nTOTAL ADA %s BLACKLIST" %(str(len(wait["blacklist"]))))
                        if WaitData == Abouts["71"]:
                          if D in meM:
                              wait["blacklist"] = {}
                              me.sendMessage(R, "delete blacklist success.!!")
                        if WaitData == Abouts["72"]:
                          if D in Owner or D in meM:
                              me.sendMessage(R,meProfile.displayName+"\nｓｅｌｆ Ｓｉａｐ ")
                              bot1.sendMessage(R,BotRangerProfile.displayName+"\nＢｏｔ1 Ｓｉａｐ")
                              bot2.sendMessage(R,BotRanger2Profile.displayName+"\nＢｏｔ2 Ｓｉａｐ")
                              bot3.sendMessage(R,BotRanger3Profile.displayName+"\nＢｏｔ3 Ｓｉａｐ")
                              bot4.sendMessage(R,BotRanger4Profile.displayName+"\nＢｏｔ4 Ｓｉａｐ")
                              bot5.sendMessage(R,BotRanger5Profile.displayName+"\nＢｏｔ5 Ｓｉａｐ")
                              bot6.sendMessage(R,BotRanger6Profile.displayName+"\nＢｏｔ6 Ｓｉａｐ")
                              bot7.sendMessage(R,BotRanger7Profile.displayName+"\nＢｏｔ7 Ｓｉａｐ")
                              bot8.sendMessage(R,BotRanger8Profile.displayName+"\nＢｏｔ8 Ｓｉａｐ")
                              bot1.sendMessage(R, "Semua Bot Sudah Siap Protect Boss.!!")
                        if WaitData.startswith(Abouts["73"]):
                          if D in meM:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]                
                            mmid = random.choice(KACOP).getContact(key1)
                            random.choice(KACOP).kickoutFromGroup(key1)
                        if WaitData.startswith(Abouts["74"]):
                          if D in meM:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]                
                            mmid = random.choice(KACOP).getContact(key1)
                            random.choice(KACOP).kickoutFromGroup(key1)
                        if WaitData.startswith(Abouts["75"]):
                          if D in Owner or D in meM:
                              if msg.toType == 2:
                                  _name = msg.text.replace(Abouts["75"],"")
                                  P = me.getGroup(R)
                                  P.preventedJoinByTicket = False
                                  me.updateGroup(P)
                                  invsend = 0
                                  Targ = me.reissueGroupTicket(R)
                                  bot1.acceptGroupInvitationByTicket(R,Targ)
                                  bot2.acceptGroupInvitationByTicket(R,Targ)
                                  bot3.acceptGroupInvitationByTicket(R,Targ)
                                  bot4.acceptGroupInvitationByTicket(R,Targ)
                                  bot5.acceptGroupInvitationByTicket(R,Targ)
                                  bot6.acceptGroupInvitationByTicket(R,Targ)
                                  bot7.acceptGroupInvitationByTicket(R,Targ)
                                  bot8.acceptGroupInvitationByTicket(R,Targ)
                                  targets = []
                                  for g in P.members:
                                      if _name in g.displayName:
                                          targets.append(g.mid)
                                  if targets == []:
                                      me.sendMessage(R, "ane limit")
                                      bot1.sendMessage(R, "ane limit juga plak")
                                      bot2.sendMessage(R, "ane limit juga plak")
                                      bot3.sendMessage(R, "ane limit juga plak")
                                      bot4.sendMessage(R, "ane limit juga plak")
                                      bot5.sendMessage(R, "ane limit juga plak")
                                      bot6.sendMessage(R, "ane limit juga plak")
                                      bot7.sendMessage(R, "ane limit juga plak")
                                      bot8.sendMessage(R, "ane limit juga plak")
                                  else:
                                      for allmember in targets:
                                          if not allmember in Bots:
                                              try:
                                                  bott=[bot1,bot2,bot3,bot4,bot5,bot6,bot7,bot8]
                                                  kikil=random.choice(bott)
                                                  kikil.kickoutFromGroup(R,[allmember])
                                              except:
                                                  bot1.sendMessage(R,"sudah limit")
                                                  bot2.sendMessage(R,"sudah limit")
                                                  bot3.sendMessage(R,"sudah limit")
                                                  bot4.sendMessage(R,"sudah limit")
                                                  bot5.sendMessage(R,"sudah limit")
                                                  bot6.sendMessage(R,"sudah limit")
                                                  bot7.sendMessage(R,"sudah limit")
                                                  bot8.sendMessage(R,"sudah limit")
                                                  me.sendMessage(R,"sudah limit")
                                      else:
                                          me.sendMessage(R,"Member kosong.!!")
                        if "Owner add: " in msg.text:
                          if msg._from in meM:
                            gid = msg.text.replace("Owner add: ","")
                            if gid == "":
                              me.sendMessage(msg.to,"Invalid Mid")
                            else:
                              if gid in Owner:
                                me.sendMessage(msg.to,"Makhluk Ini Sudah Jadi Owner Boss")
                                  #pass
                              else:
                                Owner.append(gid)
                                me.sendMessage(msg.to,"Added to Owner List")
                        if "Owner del: " in msg.text:
                          if msg._from in meM:
                            gid = msg.text.replace("Owner del: ","")
                            if gid == "":
                              me.sendMessage(msg.to,"Invalid Mid")
                            else:
                              if gid in Owner:
                                Owner.remove(gid)
                                me.sendMessage(msg.to,"Deleted From Admin List")
                              else:
                                me.sendMessage(msg.to,"This Person Not in Owner List Boss")
                        if "Leaveall" in msg.text:
                          if msg._from in meM:
                            gid = bot1.getGroupIdsJoined()
                            gid = bot2.getGroupIdsJoined()
                            gid = bot3.getGroupIdsJoined()
                            gid = bot4.getGroupIdsJoined()
                            gid = bot5.getGroupIdsJoined()
                            gid = bot6.getGroupIdsJoined()
                            gid = bot7.getGroupIdsJoined()
                            gid = bot8.getGroupIdsJoined()
                            for i in gid:
                              bot1.sendMessage(i,"Bot Has Been Expired On This Group\nPlease Contact My Owner\nThanks")
                              bot8.leaveGroup(i)
                              bot7.leaveGroup(i)
                              bot6.leaveGroup(i)
                              bot5.leaveGroup(i)
                              bot4.leaveGroup(i)
                              bot3.leaveGroup(i)
                              bot2.leaveGroup(i)
                              bot1.leaveGroup(i)
                        if WaitData == Abouts["79"]:
                          if D in Owner or D in meM:
                            if Owner == []:
                              me.sendMessage(msg.to,"Daftar List Owner Kosong")
                            else:
                              me.sendMessage(msg.to,"Tunggu...")
                              mc = "╔═══════════════════\n║👑 Owner One Piece Bot 👑\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                              for mi_d in Owner:
                                mc += "║[★]" + me.getContact(mi_d).displayName + "\n"
                              me.sendMessage(msg.to,mc)
                        if WaitData == Abouts["80"]:
                          if D in Owner or D in meM:
                            if wait["contact"] == True:
                              if wait["lang"] == "JP":
                                me.sendMessage(msg.to,"Cek Mid Lewat Share Kontak On")
                              else:
                                me.sendMessage(msg.to,"done")
                            else:
                              wait["contact"] = True
                              if wait["lang"] == "JP":
                                me.sendMessage(msg.to,"Cek Mid Lewat Share Kontak On")
                              else:
                                me.sendMessage(msg.to,"done")
                        if WaitData == ["81"]:
                          if D in Owner or D in meM:
                            if wait["contact"] == False:
                              if wait["lang"] == "JP":
                                me.sendMessage(msg.to,"Cek Mid Lewat Share Kontak Off")
                              else:
                                me.sendMessage(msg.to,"done")
                            else:
                              wait["contact"] = False
                              if wait["lang"] == "JP":
                                me.sendMessage(msg.to,"Cek Mid Lewat Share Kontak Off")
                              else:
                                me.sendMessage(msg.to,"done")
                                
                if msg.contentType == 13:
                  if wait["contact"] == True:
                    msg.contentType = 0
                    me.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                      contact = me.getContact(msg.contentMetadata["mid"])
                      try:
                        cu = me.channel.getCover(msg.contentMetadata["mid"])
                      except:
                        pass
                    else:
                      contact = me.getContact(msg.contentMetadata["mid"])
                      try:
                        cu = me.channel.getCover(msg.contentMetadata["mid"])
                      except:
                        pass
                          
        if op.type == 26:
          if wait["bot"] == True:
            msg = op.message
            text = msg.text
            Id = msg.id
            R = msg.to or to
            D = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = D
                elif msg.toType == 2:
                    to = R
                if wait["Read"] == True:
                    me.sendChatChecked(R, Id)
                if msg.contentType == 0:
                    if text is None:
                        return
                if msg.contentType == 16:
                        if wait["Shared"] == True:
                            try:
                                ret_ = "╔══[ Details Post ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = me.getContact(D)
                                    auth = "\n╠ Penulis : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n╠ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n╠ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n╠ Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n╠ Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╚══[ Finish ]"
                                me.sendMessage(R, str(ret_))
                            except Exception as error:
                                logError(error)
                                traceback.print_tb(error.__traceback__)
                if msg.contentType == 0 and D not in meM and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if meM in mention["M"]:
                                if wait["Respon"] == True:
                                    sendMention(R, D, "\n",respontags["Auto_text"])
                                    me.sendContact(R, D)
                                break
        if op.type == 19 or op.type == 32:
            Chanell = op.param1
            Penjahat = op.param2
            Kawan = op.param3
            if meM in Kawan:
                print ("SELFBOT DI KICK DARI GRUP")
                if Penjahat in Bots:
                    random.choice(KACOP).findAndAddContactsByMid(Kawan)
                    random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                    me.acceptGroupInvitation(Chanell)
                else:
                    wait["blacklist"][Penjahat] = True
                    try:
                        random.choice(KACOP).findAndAddContactsByMid(Kawan)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                        print ("BOT MENGUNDANG KEMBALI KE GRUP")
                        me.acceptGroupInvitation(Chanell)
                        random.choice(KACOP).kickoutFromGroup(Chanell,[Penjahat])
                    except:
                        Java_script.acceptGroupInvitation(Chanell)
                        Java_script2.acceptGroupInvitation(Chanell)
                        print ("SELFBOT DI KICK\nANTI JS BERTINDAK")
                        random.choice(KACJS).kickoutFromGroup(Chanell,[Penjahat])
                        P = Java_script.getGroup(Chanell)
                        P.preventedJoinByTicket = False
                        Java_script.updateGroup(P)
                        LinkQrGroup = random.choice(KACJS).reissueGroupTicket(Chanell)
                        me.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot1.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot2.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot3.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot4.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot5.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot6.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot7.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot8.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        Java_script.leaveGroup(Chanell)
                        Java_script2.leaveGroup(Chanell)
                        random.choice(KACOP).findAndAddContactsByMid(Java_scriptRanger)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Java_scriptRanger])
                        random.choice(KACOP).findAndAddContactsByMid(Java_script2Ranger)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Java_script2Ranger])
            if BotRanger in Kawan:
                print ("BOT 1 ADA YANG KICK")
                if Penjahat in Bots:
                    random.choice(KACOP).findAndAddContactsByMid(Kawan)
                    random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                    bot1.acceptGroupInvitation(Chanell)
                else:
                    wait["blacklist"][Penjahat] = True
                    try:
                        random.choice(KACOP).findAndAddContactsByMid(Kawan)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                        print ("BOT 1 DI INVITE KEMBALI")
                        bot1.acceptGroupInvitation(Chanell)
                        random.choice(KACOP).kickoutFromGroup(Chanell,[Penjahat])
                    except:
                        Java_script.acceptGroupInvitation(Chanell)
                        Java_script2.acceptGroupInvitation(Chanell)
                        print ("BOT 1 DI KICK ANTI JS BERTINDAK")
                        random.choice(KACJS).kickoutFromGroup(Chanell,[Penjahat])
                        P = Java_script.getGroup(Chanell)
                        P.preventedJoinByTicket = False
                        Java_script.updateGroup(P)
                        LinkQrGroup = Java_script.reissueGroupTicket(Chanell)
                        bot1.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        me.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot2.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot3.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot4.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot5.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot6.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot7.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot8.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        Java_script.leaveGroup(Chanell)
                        Java_script2.leaveGroup(Chanell)
                        random.choice(KACOP).findAndAddContactsByMid(Java_scriptRanger)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Java_scriptRanger])
                        random.choice(KACOP).findAndAddContactsByMid(Java_script2Ranger)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Java_script2Ranger])
            if BotRanger2 in Kawan:
                print ("BOT 2 ADA YANG KICK")
                if Penjahat in Bots:
                    random.choice(KACOP).findAndAddContactsByMid(Kawan)
                    random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                    bot2.acceptGroupInvitation(Chanell)
                else:
                    wait["blacklist"][Penjahat] = True
                    try:
                        random.choice(KACOP).findAndAddContactsByMid(Kawan)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                        print ("BOT 2 DI INVITE KEMBALI")
                        bot2.acceptGroupInvitation(Chanell)
                        random.choice(KACOP).kickoutFromGroup(Chanell,[Penjahat])
                    except:
                        Java_script.acceptGroupInvitation(Chanell)
                        Java_script2.acceptGroupInvitation(Chanell)
                        print ("BOT 2 DI KICK ANTI JS BERTINDAK")
                        random.choice(KACJS).kickoutFromGroup(Chanell,[Penjahat])
                        P = Java_script.getGroup(Chanell)
                        P.preventedJoinByTicket = False
                        Java_script.updateGroup(P)
                        LinkQrGroup = Java_script.reissueGroupTicket(Chanell)
                        bot2.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot1.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        me.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot3.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot4.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot5.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot6.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot7.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot8.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        Java_script.leaveGroup(Chanell)
                        Java_script2.leaveGroup(Chanell)
                        random.choice(KACOP).findAndAddContactsByMid(Java_scriptRanger)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Java_scriptRanger])
                        random.choice(KACOP).findAndAddContactsByMid(Java_script2Ranger)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Java_script2Ranger])
            if BotRanger3 in Kawan:
                print ("BOT 3 ADA YANG KICK")
                if Penjahat in Bots:
                    random.choice(KACOP).findAndAddContactsByMid(Kawan)
                    random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                    bot3.acceptGroupInvitation(Chanell)
                else:
                    wait["blacklist"][Penjahat] = True
                    try:
                        random.choice(KACOP).findAndAddContactsByMid(Kawan)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                        print ("BOT 3 DI INVITE KEMBALI")
                        bot3.acceptGroupInvitation(Chanell)
                        random.choice(KACOP).kickoutFromGroup(Chanell,[Penjahat])
                    except:
                        Java_script.acceptGroupInvitation(Chanell)
                        Java_script2.acceptGroupInvitation(Chanell)
                        print ("BOT 3 DI KICK ANTI JS BERTINDAK")
                        random.choice(KACJS).kickoutFromGroup(Chanell,[Penjahat])
                        P = Java_script.getGroup(Chanell)
                        P.preventedJoinByTicket = False
                        Java_script.updateGroup(P)
                        LinkQrGroup = Java_script.reissueGroupTicket(Chanell)
                        bot3.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot1.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot2.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        me.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot4.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot5.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot6.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot7.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot8.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        Java_script.leaveGroup(Chanell)
                        Java_script2.leaveGroup(Chanell)
                        random.choice(KACOP).findAndAddContactsByMid(Java_scriptRanger)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Java_scriptRanger])
                        random.choice(KACOP).findAndAddContactsByMid(Java_script2Ranger)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Java_script2Ranger])
            if BotRanger4 in Kawan:
                print ("BOT 4 ADA YANG KICK")
                if Penjahat in Bots:
                    random.choice(KACOP).findAndAddContactsByMid(Kawan)
                    random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                    bot4.acceptGroupInvitation(Chanell)
                else:
                    wait["blacklist"][Penjahat] = True
                    try:
                        random.choice(KACOP).findAndAddContactsByMid(Kawan)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                        print ("BOT 4 DI INVITE KEMBALI")
                        bot4.acceptGroupInvitation(Chanell)
                        random.choice(KACOP).kickoutFromGroup(Chanell,[Penjahat])
                    except:
                        Java_script.acceptGroupInvitation(Chanell)
                        Java_script2.acceptGroupInvitation(Chanell)
                        print ("BOT 4 DI KICK ANTI JS BERTINDAK")
                        random.choice(KACJS).kickoutFromGroup(Chanell,[Penjahat])
                        P = Java_script.getGroup(Chanell)
                        P.preventedJoinByTicket = False
                        Java_script.updateGroup(P)
                        LinkQrGroup = Java_script.reissueGroupTicket(Chanell)
                        bot4.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot1.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot2.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot3.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        me.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot5.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot6.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot7.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot8.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        Java_script.leaveGroup(Chanell)
                        Java_script2.leaveGroup(Chanell)
                        random.choice(KACOP).findAndAddContactsByMid(Java_scriptRanger)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Java_scriptRanger])
                        random.choice(KACOP).findAndAddContactsByMid(Java_script2Ranger)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Java_script2Ranger])
            if BotRanger5 in Kawan:
                print ("BOT 5 ADA YANG KICK")
                if Penjahat in Bots:
                    random.choice(KACOP).findAndAddContactsByMid(Kawan)
                    random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                    bot5.acceptGroupInvitation(Chanell)
                else:
                    wait["blacklist"][Penjahat] = True
                    try:
                        random.choice(KACOP).findAndAddContactsByMid(Kawan)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                        print ("BOT 5 DI INVITE KEMBALI")
                        bot5.acceptGroupInvitation(Chanell)
                        random.choice(KACOP).kickoutFromGroup(Chanell,[Penjahat])
                    except:
                        Java_script.acceptGroupInvitation(Chanell)
                        Java_script2.acceptGroupInvitation(Chanell)
                        print ("BOT 5 DI KICK ANTI JS BERTINDAK")
                        random.choice(KACJS).kickoutFromGroup(Chanell,[Penjahat])
                        P = Java_script.getGroup(Chanell)
                        P.preventedJoinByTicket = False
                        Java_script.updateGroup(P)
                        LinkQrGroup = Java_script.reissueGroupTicket(Chanell)
                        bot5.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot1.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot2.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot3.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot4.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        me.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot6.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot7.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot8.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        Java_script.leaveGroup(Chanell)
                        Java_script2.leaveGroup(Chanell)
                        random.choice(KACOP).findAndAddContactsByMid(Java_scriptRanger)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Java_scriptRanger])
                        random.choice(KACOP).findAndAddContactsByMid(Java_script2Ranger)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Java_script2Ranger])
            if BotRanger6 in Kawan:
                print ("BOT 6 ADA YANG KICK")
                if Penjahat in Bots:
                    random.choice(KACOP).findAndAddContactsByMid(Kawan)
                    random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                    bot6.acceptGroupInvitation(Chanell)
                else:
                    wait["blacklist"][Penjahat] = True
                    try:
                        random.choice(KACOP).findAndAddContactsByMid(Kawan)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                        print ("BOT 6 DI INVITE KEMBALI")
                        bot6.acceptGroupInvitation(Chanell)
                        random.choice(KACOP).kickoutFromGroup(Chanell,[Penjahat])
                    except:
                        Java_script.acceptGroupInvitation(Chanell)
                        Java_script2.acceptGroupInvitation(Chanell)
                        print ("BOT 6 DI KICK ANTI JS BERTINDAK")
                        random.choice(KACJS).kickoutFromGroup(Chanell,[Penjahat])
                        P = Java_script.getGroup(Chanell)
                        P.preventedJoinByTicket = False
                        Java_script.updateGroup(P)
                        LinkQrGroup = Java_script.reissueGroupTicket(Chanell)
                        bot6.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot1.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot2.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot3.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot4.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot5.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        me.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot7.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot8.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        Java_script.leaveGroup(Chanell)
                        Java_script2.leaveGroup(Chanell)
                        random.choice(KACOP).findAndAddContactsByMid(Java_scriptRanger)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Java_scriptRanger])
                        random.choice(KACOP).findAndAddContactsByMid(Java_script2Ranger)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Java_script2Ranger])
            if BotRanger7 in Kawan:
                print ("BOT 7 ADA YANG KICK")
                if Penjahat in Bots:
                    random.choice(KACOP).findAndAddContactsByMid(Kawan)
                    random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                    bot7.acceptGroupInvitation(Chanell)
                else:
                    wait["blacklist"][Penjahat] = True
                    try:
                        random.choice(KACOP).findAndAddContactsByMid(Kawan)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                        print ("BOT 7 DI INVITE KEMBALI")
                        bot7.acceptGroupInvitation(Chanell)
                        random.choice(KACOP).kickoutFromGroup(Chanell,[Penjahat])
                    except:
                        Java_script.acceptGroupInvitation(Chanell)
                        Java_script2.acceptGroupInvitation(Chanell)
                        print ("BOT 7 DI KICK ANTI JS BERTINDAK")
                        random.choice(KACJS).kickoutFromGroup(Chanell,[Penjahat])
                        P = Java_script.getGroup(Chanell)
                        P.preventedJoinByTicket = False
                        Java_script.updateGroup(P)
                        LinkQrGroup = Java_script.reissueGroupTicket(Chanell)
                        bot7.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot1.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot2.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot3.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot4.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot5.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot6.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        me.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot8.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        Java_script.leaveGroup(Chanell)
                        Java_script2.leaveGroup(Chanell)
                        random.choice(KACOP).findAndAddContactsByMid(Java_scriptRanger)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Java_scriptRanger])
                        random.choice(KACOP).findAndAddContactsByMid(Java_script2Ranger)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Java_script2Ranger])
            if BotRanger8 in Kawan:
                print ("BOT 8 ADA YANG KICK")
                if Penjahat in Bots:
                    random.choice(KACOP).findAndAddContactsByMid(Kawan)
                    random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                    bot8.acceptGroupInvitation(Chanell)
                else:
                    wait["blacklist"][Penjahat] = True
                    try:
                        random.choice(KACOP).findAndAddContactsByMid(Kawan)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                        print ("BOT 8 DI INVITE KEMBALI")
                        bot8.acceptGroupInvitation(Chanell)
                        random.choice(KACOP).kickoutFromGroup(Chanell,[Penjahat])
                    except:
                        Java_script.acceptGroupInvitation(Chanell)
                        Java_script2.acceptGroupInvitation(Chanell)
                        print ("BOT 8 DI KICK ANTI JS BERTINDAK")
                        random.choice(KACJS).kickoutFromGroup(Chanell,[Penjahat])
                        P = Java_script.getGroup(Chanell)
                        P.preventedJoinByTicket = False
                        Java_script.updateGroup(P)
                        LinkQrGroup = Java_script.reissueGroupTicket(Chanell)
                        bot8.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot1.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot2.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot3.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot4.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot5.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot6.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot7.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        me.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        Java_script.leaveGroup(Chanell)
                        Java_script2.leaveGroup(Chanell)
                        random.choice(KACOP).findAndAddContactsByMid(Java_scriptRanger)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Java_scriptRanger])
                        random.choice(KACOP).findAndAddContactsByMid(Java_script2Ranger)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Java_script2Ranger])
            if Java_scriptRanger in Kawan:
                print ("ANTI JS 1 DI KICK")
                if Penjahat in Bots:
                    random.choice(KACOP).findAndAddContactsByMid(Kawan)
                    random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                else:
                    wait["blacklist"][Penjahat] = True
                    try:
                        random.choice(KACOP).findAndAddContactsByMid(Kawan)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                        print ("ANTI JS 1 DI INVITE")
                        random.choice(KACOP).kickoutFromGroup(Chanell,[Penjahat])
                    except:
                        me.findAndAddContactsByMid(Kawan)
                        me.inviteIntoGroup(Chanell,[Kawan])
                        print ("ANTI JS 1 DI INVITE")
                        random.choice(KACOP).kickoutFromGroup(Chanell,[Penjahat])
            if Java_script2Ranger in Kawan:
                print ("ANTI JS 2 DI KICK")
                if Penjahat in Bots:
                    random.choice(KACOP).findAndAddContactsByMid(Kawan)
                    random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                else:
                    wait["blacklist"][Penjahat] = True
                    try:
                        random.choice(KACOP).findAndAddContactsByMid(Kawan)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Kawan])
                        print ("ANTI JS 2 DI INVITE")
                        random.choice(KACOP).kickoutFromGroup(Chanell,[Penjahat])
                    except:
                        me.findAndAddContactsByMid(Kawan)
                        me.inviteIntoGroup(Chanell,[Kawan])
                        print ("ANTI JS 2 DI INVITE")
                        random.choice(KACOP).kickoutFromGroup(Chanell,[Penjahat])
        if op.type == 19 or op.type == 32:
            Chanell = op.param1
            Penjahat = op.param2
            Kawan = op.param3
            if Chanell in wait["PROTECT"]:
                if Penjahat in Bots or Penjahat in Owner:
                    pass
                else:
                    wait["blacklist"][Penjahat] = True
                    print ("PROTECT BERTINDAK DI GRUP "+me.getGroup(Chanell).name)
                    try:
                        random.choice(KACOP).kickoutFromGroup(Chanell,[Penjahat])
                    except:
                        random.choice(KACOP).kickoutFromGroup(Chanell,[Prnjahat])
        if op.type == 17:
            Chanell = op.param1
            Penjahat = op.param2
            Kawan = op.param3
            if Penjahat in wait["blacklist"]:
                print ("BLACKLIST MASUK DI GRUP "+me.getGroup(Chanell).name)
                try:
                    random.choice(KACOP).kickoutFromGroup(Chanell,[Penjahat])
                    random.choice(KACOP).sendMessage(R,"Mahluk Tersebut Ada Di Daftar BlackList Plak\nJadi Kami Kick\nHapus Dulu Dari Blacklist")
                except:
                    random.choice(KACOP).kickoutFromGroup(Chanell,[Prnjahat])
                    random.choice(KACOP).sendMessage(R,"Mahluk Tersebut Ada Di Daftar BlackList Plak\nJadi Kami Kick\nHapus Dulu Dari Blacklist")
            else:pass
        if op.type == 13:
            Chanell = op.param1
            Penjahat = op.param2
            Kawan = op.param3
            if Penjahat in Bots or Penjahat in Owner:
              pass
            else:
              if Kawan in wait["blacklist"]:
                print ("BLACKLIST DI INVITE DI GRUP "+me.getGroup(Chanell).name)
                try:
                    random.choice(KACOP).cancelGroupInvitation(Chanell,[Kawan])
                    random.choice(KACOP).kickoutFromGroup(Chanell,[Penjahat])
                    random.choice(KACOP).sendMessage(R,"Mahluk Tersebut Ada Di Daftar BlackList Plak\nJadi Kami Cancel\nHapus Dulu Dari Blacklist")
                    random.choice(KACOP).sendMessage(R,"Silahkan Cek Siapa Yang Undang Blacklist Ke Sini Plak")
                except:
                    random.choice(KACOP).cancelGroupInvitation(Chanell,[Kawan])
                    random.choice(KACOP).kickoutFromGroup(Chanell,[Penjahat])
                    random.choice(KACOP).sendMessage(R,"Mahluk Tersebut Ada Di Daftar BlackList Plak\nJadi Kami Cancel\nHapus Dulu Dari Blacklist")
                    random.choice(KACOP).sendMessage(R,"Silahkan Cek Siapa Yang Undang Blacklist Ke Sini Plak")
            if Chanell in wait["PROTECT"]:
                if Penjahat in Bots or Penjahat in Owner:
                    pass
                else:
                    wait["blacklist"][Penjahat] = True
                    print ("PROTECT BERTINDAK DI GRUP "+me.getGroup(Chanell).name)
                    try:
                        random.choice(KACOP).cancelGroupInvitation(Chanell,[Kawan])
                        random.choice(KACOP).kickoutFromGroup(Chanell,[Penjahat])
                    except:
                        random.choice(KACOP).cancelGroupInvitation(Chanell,[Kawan])
                        random.choice(KACOP).kickoutFromGroup(Chanell,[Penjahat])
        if op.type == 11:
            Chanell = op.param1
            Penjahat = op.param2
            Kawan = op.param3
            if Chanell in wait["PROTECT"]:
                if Penjahat in Bots or Penjahat in Owner:
                    pass
                else:
                    wait["blacklist"][Penjahat] = True
                    print ("PROTECT BERTINDAK DI GRUP "+me.getGroup(Chanell).name)
                    try:
                        P = bot1.getGroup(Chanell)
                        P.preventedJoinByTicket = True
                        bot1.updateGroup(P)
                        random.choice(KACOP).kickoutFromGroup(Chanell,[Penjahat])
                    except:
                        Java_script.acceptGroupInvitation(Chanell)
                        Java_script2.acceptGroupInvitation(Chanell)
                        P = bot1.getGroup(Chanell)
                        P.preventedJoinByTicket = True
                        bot1.updateGroup(P)
                        random.choice(KACJS).kickoutFromGroup(Chanell,[Penjahat])
                        Java_script.leaveGroup(Chanell)
                        Java_script2.leaveGroup(Chanell)
                        random.choice(KACOP).findAndAddContactsByMid(Java_scriptRanger)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Java_scriptRanger])
                        random.choice(KACOP).findAndAddContactsByMid(Java_script2Ranger)
                        random.choice(KACOP).inviteIntoGroup(Chanell,[Java_script2Ranger])
        if op.type == 13:
            print ("NOTIFIED MEMBER OR SELF JOIN GROUP")
            Gr = op.param1
            if wait["Join"] == True:
                me.acceptGroupInvitation(Gr)
            else:
                pass
        if op.type == 5:
            print ("NOTIFIED ADD CONTACT SELF")
            if wait["Add"] == True:
                me.findAndAddContactsByMid(op.param1)
            sendMention(op.param1, op.param1, "Thanks For add Me ","")
        if op.type == 15:
            Gr = op.param1
            Cj = op.param2
            print ("NOTIFIED CONTACT MEMBER LEAVE TO GROUP")
            if wait["Wc"] == True:
                Gc = me.getGroup(Gr)
                dia = me.getContact(Cj)
                ms = "Bye : {}".format(dia.displayName)
                ms += "In group : {}".format(Gc.name)
                mt = "Kenapa Kamu Keluar Group? {}".format(Gc.name)
                me.sendMessage(Gr,str(ms))
                me.sendMessage(dia,mt)
                me.sendContact(Gr,dia)
        if op.type == 17:
            Gr = op.param1
            Cj = op.param2
            print ("NOTIFIED CONTACT MEMBER JOIN TO GROUP")
            if wait["Wc"] == True:
                Gc = me.getGroup(Gr)
                dia = me.getContact(Cj)
                ms = "Welcome : {}".format(dia.displayName)+" In group : {}".format(Gc.name)
                me.sendMessage(Gr,str(ms))
                me.sendContact(Gr,dia)
        if op.type == 65:
            print ("UNSEND MESSAGE UNSENDER FROM MY SELF")
            if wait["Unsend"] == True:
                Geting = op.param1
                Text_in_Destroy = op.param2
                if Text_in_Destroy in msg_dict:
                    Timer = time.time()
                    Target_Text = me.getContact(msg_dict[Text_in_Destroy]["from"])
                    if "text" in msg_dict[Text_in_Destroy]:
                        StartTimer = Timer - msg_dict[Text_in_Destroy]["waktu"]
                        StartTimer = format_timespan(StartTimer)
                        rat_ = "Timer unsend: {} WIB".format(StartTimer)
                        rat_ += "Text Unsend\n{}".format(msg_dict[Text_in_Destroy]["text"])
                        sendMention(Geting, Target_Text.mid, "Sorry\nMy Resend your Message\n\n", str(rat_))
                        del msg_dict[Text_in_Destroy]
                else:
                    me.sendMessage(Geting,"Detected Unsend")
        if op.type == 55:
          try:
            group_id = op.param1
            user_id=op.param2
            subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
          except Exception as e:
              print (e)
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                          if op.param2 in Owner:
                            pass
                          else:
                            Name = me.getContact(op.param2).displayName
                            Np = me.getContact(op.param2).pictureStatus
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        me.sendMessage(op.param1, "Woy " + "☞ " + nick[0] + " ☜" + "\nDasar Cicitipi")
                                        me.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                    else:
                                        me.sendMessage(op.param1, "Woy " + "☞ " + nick[1] + " ☜" + "\nBetah Banget Jadi Cicitipi. . .\nChat Woy (-__-)   ")
                                        me.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                else:
                                    me.sendMessage(op.param1, "Jiahahaha " + "☞ " + Name + " ☜" + "\nNgapain Cicitipi Doang???\nGa Gaul Lu ga Mau Chat\nPasti Temennya Dikit ")
                                    me.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass
        else:
            pass
              
    except Exception as error:
        ErrorX(error)
        if op.type == 59:
            print (op)
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          oepoll.setRevision(op.revision)
    except Exception as e:
        me.log("DATA: " + str(e))
