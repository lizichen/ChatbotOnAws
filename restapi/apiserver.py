from utils import log
from insta_scrapping import getNumberOfInstaPosts
from bottle import route, run, request
import json
import requests

AI_URL = 'https://dev.customerserviceai.com:9912/'
fb_session = 'fb_sesoin'
domain = 'cudeeplearning17' # llcao's class at Columbia


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
				send_message(sender_id, answer_from_ai(message_text))
                #send_message(sender_id, getNumberOfInstaPosts(message_text))
                #getInstaImages(sender_id, message_text)
   return "ok"

def answer_from_ai(message_text):
    AI_response =  requests.post(AI_URL + 'top_faq_answers',
                                     json={'domain': domain, 'question': message_text, 'sessionid': fb_session})
    AI_response_dict = json.loads(AI_response.content)
    if AI_response_dict['success']:
        print 'successfully call AI!'
        if 0:
            print 'keys are:', AI_response_dict.keys()
        
        #print 'best answer:', AI_response_dict['answers'][0]
        return AI_response_dict['answers'][0]
		# print 'score=', AI_response_dict['scores'][0]
        # print 'Is the best answer more confident than the threshold?', AI_response_dict['scores'][0] > AI_response_dict['thresh']
    else:
        print 'failed to call AI, err_msg=', AI_response_dict['err_msg']    

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



   






