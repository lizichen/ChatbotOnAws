# Deploy Facebook Chatbot Messenger on an Amazon AWS Instance

### Tasks

- Obtain a domain name from NameCheap.com (or any domain name retailer).
- Link domain name with AWS EC2 IP address.
- Obtain SSL Certificate for the secured HTTPS protocal, which is required by Facebook Messenger Platform. 
  - Install certbot for Apache Web Server on Ubuntu 16.04
  - Configure Bottlepy (WSGI Python Web Application Framework) for Apache Web Server

### Install Apache2 and Obtain SSL Certificate for the domain name
- sudo apt-get install apache2
- sudo apt-get install python-letsencrypt-apache
- set up a CNAME for the ip (e.g. elastic IP + Route 53).
  - Copy AWS instance Public DNS (IPv4) name. i.e., ec1-23-456-789-012.compute-1.amazonaws.com
  - Connect it on NameCheap.com with new Host Record of type 'CNAME Record'.  
- sudo letsencrypt --apache -d yourdomainname.com
- sudo service apache2 restart

### Configure Bottlepy for Apache
- sudo pip install bottle
- sudo apt-get install libapache2-mod-wsgi
- under /var/www/, create directory /restapi
- under /restapi directory, create sample python bottle script.
- under /etc/apache2/sites-enabled/ directory, modify the file 000-default-le-ssl.conf as following:
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
- sudo service apache2 restart
- tail -200f /var/log/apache2/error.log

### Install MongoDB and PyMongo
- Import public key for Ubuntu Package Management System
```sh
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
```
- Create a list file for MongoDB
```sh
echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
```
- Reload local package database
```sh
sudo apt-get update
```
- install the MongoDB packages
```sh
sudo apt-get install -y mongodb-org
```
- Start MongoDB
```sh
sudo service mongod start
```
- Verify MongoDB
```sh
tail /var/log/mongodb/mongod.log
```
- Port Config
```sh
/etc/mongod.conf
```
- Stop MongoDB
```sh
sudo service mongod stop
```
- Install PyMongo
```sh
sudo pip install pymongo
sudo pip install --upgrade pymongo
```

### Installations of other modules (may not be used)
- sudo apt-get update
- sudo pip install pandas
- sudo apt-get install python-bs4



