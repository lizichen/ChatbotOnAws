from bottle import route, run, request
import json
import requests

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
   print "inside POST webhook"
   
   data = request.json
   if data["object"] == "page":
      for entry in data["entry"]:
         for messaging_event in entry["messaging"]:
            if messaging_event.get("message"):  # someone sent us a message
               sender_id = messaging_event["sender"]["id"]   
               recipient_id = messaging_event["recipient"]["id"]
               message_text = messaging_event["message"]["text"]
               send_message(sender_id, "got it, thanks!")
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

def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)

