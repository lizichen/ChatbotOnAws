import sys
import os
import json
import requests

AI_URL = 'https://dev.customerserviceai.com:9912/'

fb_session = 'fb_sesoin'

domain = 'cudeeplearning17' # llcao's class at Columbia

question = 'what textbook to use' # feel free to change this

AI_response = requests.post(AI_URL + 'top_faq_answers',
                                     json={'domain': domain, 'question': question, 'sessionid': fb_session})

AI_response_dict = json.loads(AI_response.content)
if AI_response_dict['success']:
    print 'successfully call AI!'
    if 0:
        print 'keys are:', AI_response_dict.keys()

    print 'best answer:', AI_response_dict['answers'][0]
    print 'score=', AI_response_dict['scores'][0]
    print 'Is the best answer more confident than the threshold?', AI_response_dict['scores'][0] > AI_response_dict['thresh']

else:
    print 'failed to call AI, err_msg=', AI_response_dict['err_msg']
