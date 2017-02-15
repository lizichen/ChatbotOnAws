from utils import log
from insta_scrapping import getNumberOfInstaPosts
from bottle import route, run, request
import json
import requests

#import socket
#local_ip = socket.gethostbyname(socket.gethostname())

#import pymongo
#from bson.objectid import ObjectId
#CLIENT = pymongo.MongoClient()
#user_db = CLIENT.userDB

#page_access_token = "EAAB0vKbZBLtUBAJEfOZALjxZCJMmIeKElqumlZCmYvkBmeYs1wbz3Tlz2XCngxvZBhvkOVkTgbiOFur3OgzTEAoaqeyvZAPBv3R5JBgfMAkXrnZCihKdVLI6rbGv8DPYZAljS2PfDXDZCBfwusx4IJ1IUqE6CltZBjINbAizhQRhDXGAZDZD"
page_access_token = "EAASXZB3dJrOMBAOU0A2ZBi0fmnht2o7Crw0kWUcH9aZAZAraZAknrDugsLjuBA13ZAs4IaFDrZBRMor6Jw8uIAinPEg8uXYWeTHnjPOZBLBaxMJvTEftQ1fjmeXsosblyQuHCZCwGQ5yvsgA7gMjgcjcaQRlZBYuDV8xcvNkUKLETZCvwZDZD"

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
    return "Okay!"

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
               #getInstaImages(sender_id, message_text)
   return "ok"

def send_message(recipient_id, message_text):
    print str("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))
    params = {"access_token":page_access_token}
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"recipient": {"id": recipient_id},
        "message": {"text": message_text}
    })
    #row = {'user': recipient_id, "message_text": message_text}
    #first_table = user_db['first_table']
    #first_table.save(row)
    #print 'grabbing after inserting:' , list(first_table.find({'user':recipient_id}))
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)



   






