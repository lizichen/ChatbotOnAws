
import datetime
from bson.objectid import ObjectId
import os, sys

class FB_ChatSessionTable(CustomerServiceTable):
### one session per row ###
	
    {
        '_id': sessionid
    	'user':
    	'client_addr':    #'server_addr': ''    # to be replace with webpage
    	'start_time':
     	'expire_time':
     	'chats': [chat, chat ,...]
            list of chat records
            {
            'question':
            'received_at':
            'typing_secs':
            #'first_answer':
            #'first_answer_score':
            #'ai_thresh':
            #'answered_at':
            'answers':[
                {
                'answer':
                'score':
                'answered_after':
                },
                ...
                ]
            }
    }

