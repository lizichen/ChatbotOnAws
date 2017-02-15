import datetime
import pymongo
from bson.objectid import ObjectId

import socket
local_ip = socket.gethostbyname(socket.gethostname())
CLIENT = pymongo.MongoClient(local_ip,443)

if __name__ == '__main__':


    # connect to db
    lizi_db = CLIENT.lizidb
    print lizi_db

    # grab rows
    lizi_table = lizi_db['first_table']
    print 'first grabbing:', list(lizi_table.find({'user':'lizi'}))

    # insert row
    row = {'user':'lizi', 'hobby':'jumping'}
    lizi_table.save(row)

    # grab rows
    lizi_table = lizi_db['first_table']
    print 'grabbing after inserting:', list(lizi_table.find({'user': 'lizi'}))


