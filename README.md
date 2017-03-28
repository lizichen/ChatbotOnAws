# Deploy Facebook Chatbot Messenger

### Groundwork 
- Create [Facebook Page][create-fb-page] and [Facebook App][create-fb-app]
- Obtain a domain name from [NameCheap.com][namecheap] (or any domain name retailer).
- Initialize [AWS EC2 Instance (Ubuntu)][aws] and link domain name with AWS EC2 IP address, this is done on the NameCheap DNS set-up page.
  + Set up a **CNAME** for the ip (e.g. elastic IP + Route 53).
  + Copy **AWS instance Public DNS (IPv4)** name. i.e., ec1-23-456-789-012.compute-1.amazonaws.com
  + Connect it on NameCheap.com with new *Host Record* of type **'CNAME Record'**.  
- Install **Apache2** on Ubuntu 16.04:   
    ```bash
      sudo apt-get install apache2
    ```
- Obtain **SSL Certificate** for the secured HTTPS protocal. (This is required by Facebook Messenger Platform.) 
  - Install [certbot][certbot] for Apache Web Server on Ubuntu 16.04:     
    ```bash
      sudo apt-get install python-letsencrypt-apache
    ```
    <br />
    ```bash
      sudo letsencrypt --apache -d yourdomainname.com
    ```
    <br />
    ```bash
      sudo service apache2 restart
    ```
  - Configure [Bottlepy][bottlepy] (WSGI Python Web Application Framework) for Apache Web Server
    + Install **Bottlepy**:   
      ```bash
        sudo pip install bottle
      ```
    + install **WSGI** interface:   
      ```bash
        sudo apt-get install libapache2-mod-wsgi
      ```
    + Under /var/www/, create directory /restapi (A dir that contains the web app code.)
    + under /restapi directory, create sample Bottlepy script.
    + under /etc/apache2/sites-enabled/ directory, modify the file **000-default-le-ssl.conf** as following:   
      ```bash
          ServerAdmin webmaster@localhost
              DocumentRoot    /var/www/restapi
              WSGIScriptAlias /               /var/www/restapi/restapi.wsgi
              WSGIDaemonProcess       restapi    threads=25
              WSGIScriptReloading     Off

          <Directory /var/www>
              Order allow,deny
              Allow from all
          </Directory>

          <Directory /var/www/restapi>
              WSGIProcessGroup restapi
              WSGIApplicationGroup %{GLOBAL}
              Order deny,allow
              Allow from all
          </Directory>
      ```
    + *Restart* Apache Web Server:   
      ```bash
        sudo service apache2 restart
      ```
    + Tail the log to monitor what's happening:  
      ```bash
        tail -200f /var/log/apache2/error.log
      ```

### Configure Facebook Tokens:
To set up webhook, use of PAGE_ACCESS_TOKEN etc. A Facebook Tutorial: [Link][fb-tutorial]

### Receive Msg and Return Msg:

```python
#An input msg comes in:
@route('/webhook', method=['POST'])
def receiveMsgAndSendBackStuff():
   data = request.json
   if data["object"] == "page":
      for entry in data["entry"]:
         for messaging_event in entry["messaging"]:
      if messaging_event.get("message"): 
        sender_id = messaging_event["sender"]["id"]   
        recipient_id = messaging_event["recipient"]["id"]
        message_text = messaging_event["message"]["text"]
        send_message(sender_id, message_text)

#Reply an msg:
def send_message(recipient_id, message_text):
    params = {"access_token":page_access_token} #pre-set PAGE_ACCESS_TOKEN from the Facebook App Set-up page
    headers = {"Content-Type": "application/json"} #it's a json obj
    data = json.dumps({"recipient": {"id": recipient_id},
        "message": {"text": "Hello!"} #reply with a string 'Hello!'
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
```

### Integration of AI response:
Visit: [http://www.customerserviceai.com][http://www.customerserviceai.com/]

### Facebook APP Go Live:
1. Create Mock Testers and Test Cases. (Under the Roles subpage in the FB App Dashboard)
2. Create Submission and add example auto replies for the reviewers.
3. Indicate which Mock Tester(s) can be used for the reviewers. (at the *App Verification Note* box)
4. At the Dashboard Setting subpage, add **Privacy Policy URL** and **Terms of Service URL** for app review.
5. Submit for Review!


[create-fb-page]:https://www.facebook.com/pages/create/
[create-fb-app]:https://developers.facebook.com/apps
[namecheap]:https://www.namecheap.com/
[aws]:aws.amazon.com
[certbot]:https://certbot.eff.org/#ubuntuxenial-apache
[bottlepy]:bottlepy.org
[fb-tutorial]: https://developers.facebook.com/docs/messenger-platform/guides/quick-start 
[http://www.customerserviceai.com/]: http://www.customerserviceai.com/
