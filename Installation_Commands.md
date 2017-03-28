## Commands for Package Installation and Usage

### Install MongoDB and PyMongo
- Import *public key* for Ubuntu Package Management System   
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
  ```
  <br />
  ```  
    sudo pip install --upgrade pymongo
  ```

### Installations of other modules, etc (may not be used)
- sudo apt-get update
- sudo pip install pandas
- sudo apt-get install python-bs4