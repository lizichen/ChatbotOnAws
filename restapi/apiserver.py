from bottle import route, run, request
import json
import requests

# for instagram post scraping
from bs4 import BeautifulSoup
from pandas.io.json import json_normalize
import unicodedata
import datetime

@route('/hello')
def index():
        return "hello"

@route('/webhook', method=['GET'])
def facebookWebHook():
    print request.query.get("hub.mode")
    print request.query.get("hub.challenge")
    print request.query.get("hub.verify_token")
    if request.query.get("hub.mode") == "subscribe" and request.query.get("hub.challenge"):
        if request.query.get("hub.verify_token") == "testbot_verify_token":
	    return request.query.get("hub.challenge")
    return "Hello world"

@route('/webhook', method=['POST'])
def receiveMsgAndSendBackStuff():
   data = request.json
   if data["object"] == "page":
      for entry in data["entry"]:
         for messaging_event in entry["messaging"]:
            if messaging_event.get("message"):  # someone sent us a message
               sender_id = messaging_event["sender"]["id"]   
               recipient_id = messaging_event["recipient"]["id"]
               message_text = messaging_event["message"]["text"]
               send_message(sender_id, getNumberOfInstaPosts(message_text))
   return "ok"

def send_message(recipient_id, message_text):
    print str("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))
    params = {
	"access_token":"EAASXZB3dJrOMBAHptbpYthEDQENypgXrSbiMM2XuHEAFz2oabH2tH7bczWG1UAmTQGVjqrXt5pzvISU9xVYWgOZAveW5DVOr3AZBNpaCB18RoSva5TDx0ilZBANCSC4kKPSEXpgFji8YAonqEI7LVqsEM1AZASCiR4GDd9QZAyVgZDZD"
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)

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

def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)

