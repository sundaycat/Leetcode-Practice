class Message(object):

    def __init__(self, sender, recipient, conversationId):
        self.sender = sender
        self.recipient = recipient
        self.conversationId = conversationId

def get_responseive_rate(biz_owner_id, msg_list):
    if not msg_list or len(msg_list) == 0:
        return 0

    send = set()
    reci = set()
    for i in range(0, len(msg_list)):
        cursor = msg_list[i]
        if cursor.sender == biz_owner_id:
            send.add(cursor.conversationId)

        if cursor.recipient == biz_owner_id:
            reci.add(cursor.conversationId)

    num_of_send = len(send)
    num_of_reci = len(reci)

    # corner case, the denominator is 0
    if num_of_reci == 0:
        return 0

    return int(num_of_send / num_of_reci * 100)


# sender, recipient, conversation
m1 = Message(1, 42, 1)
m2 = Message(42, 1, 1)
m3 = Message(2, 42, 2)
m4 = Message(2, 42, 2)
m5 = Message(3, 88, 3)
m6 = Message(3, 42, 4)

msg_list = [m1, m2, m3, m4, m5, m6]
print(get_responseive_rate(42, msg_list))
