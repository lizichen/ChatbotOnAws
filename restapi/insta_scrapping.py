# for instagram post scraping
from bs4 import BeautifulSoup
from pandas.io.json import json_normalize
import unicodedata
import datetime
import requests
import json

def getNumberOfInstaPosts(uid):
    r = requests.get("https://www.instagram.com/"+uid)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    body = soup.find("body")
    body = body.find("script", {"type":"text/javascript"}).text
    body = unicodedata.normalize('NFKD', body).encode('ascii','ignore')
    body_len = len(body)
    body = body[21:body_len-1]
    data = json.loads(body)
    l = data["entry_data"]["ProfilePage"]
    l = l.pop()
    numberOfPosts = l["user"]["media"]["count"]
    listOfPosts = l["user"]["media"]["nodes"]
    try:
        latestPost = listOfPosts[0]
        unixTimestamp = latestPost["date"]
        latestPostTime = datetime.datetime.fromtimestamp(unixTimestamp).strftime('%Y-%m-%d %H:%M:%S')
    except:
        latestPostTime = "N/A"
    return "Number of Posts:"+str(numberOfPosts)+" Latest Post at:"+latestPostTime

def getInstaImages(senderID, uid):
    r = requests.get("https://www.instagram.com/"+uid)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    body = soup.find("body")
    body = body.find("script", {"type":"text/javascript"}).text
    body = unicodedata.normalize('NFKD', body).encode('ascii','ignore')
    body_len = len(body)
    body = body[21:body_len-1]
    data = json.loads(body)
    l = data["entry_data"]["ProfilePage"]
    l = l.pop()
    numberOfPosts = l["user"]["media"]["count"]
    listOfPosts = l["user"]["media"]["nodes"]
    try:
        latestPost = listOfPosts[0]
        unixTimestamp = latestPost["date"]
        code = latestPost["code"]
        thumbnail_src = latestPost["thumbnail_src"]
        latestPostTime = datetime.datetime.fromtimestamp(unixTimestamp).strftime('%Y-%m-%d %H:%M:%S')

        inst_url = "https://www.instagram.com/p/" + code + "/?taken-by=" + uid
        print inst_url
        print thumbnail_src
        print "message constructed\n"
        params = {"access_token":"EAASXZB3dJrOMBAHptbpYthEDQENypgXrSbiMM2XuHEAFz2oabH2tH7bczWG1UAmTQGVjqrXt5pzvISU9xVYWgOZAveW5DVOr3AZBNpaCB18RoSva5TDx0ilZBANCSC4kKPSEXpgFji8YAonqEI7LVqsEM1AZASCiR4GDd9QZAyVgZDZD"}
        headers = {"Content-Type":"application/json"}
        data = json.dumps({
            "recipient":{id: senderID},
            "message":{
               "attachment": {
                   "type":"image",
                   "payload":{ "url" : "https://yt3.ggpht.com/-v0soe-ievYE/AAAAAAAAAAI/AAAAAAAAAAA/OixOH_h84Po/s900-c-k-no-mo-rj-c0xffffff/photo.jpg" }
                }
            }
        })
        r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    except:
        latestPostTime = "N/A"
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)
