

def sendMsgToSWITI(msg_text, recipient_id):
    domain = "cudeeplearning17"
    accounttable = AccountTable()
    user_rows = accounttable.query_rows_aslist({'user':domain})
    if not user_rows or len(user_rows) == 0:
        print "ERROR! no user_row!"
    connect_response_dict = {}




