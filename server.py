
#!/usr/bin/env python3

"""Server for multithreaded (asynchronous) chat application."""

from socket import AF_INET, socket, SOCK_STREAM

from threading import Thread
online=[]
sender_list=[]



def accept_incoming_connections():

    """Sets up handling for incoming clients."""

    while True:

        client, client_address = SERVER.accept()

        print("%s:%s has connected." % client_address)

        #client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))

        addresses[client] = client_address
        

        Thread(target=handle_client, args=(client,)).start()





def handle_client(client):  # Takes client socket as argument.

    """Handles a single client connection."""



    name = client.recv(BUFSIZ).decode("utf8")

   # welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name

    #client.send(bytes(welcome, "utf8"))
    online.append(name)

    #msg = "%s has joined the chat!" % name
    #msg+='@join'
    #print(online)
    
    msg=''
    for i in online:
        msg=msg+i
        msg=msg+'@*'
    if len(online)>0:
        client.send(bytes(msg, "utf8"))
        broadcast(bytes(msg, "utf8"))
    
    clients[client] = name



    while True:

        msg = client.recv(BUFSIZ)
        global sender_list
        #print(msg==bytes("*quit*", "utf8"))
        if msg !=bytes("*quit*", "utf8"):
            msg=msg.decode("utf-8")#convert bytes to string
            temp_list=msg.split('@_*')
            sender_list=temp_list[1:-1]
            msg=temp_list[0].encode("utf-8")#convert string to bytes
            if len(sender_list)==0:
                broadcast(msg, name+": ")
            else:
                chosen_cast(msg, name+": ")
            #broadcast(msg, name+": ")

        else:
            #print("Akash")
            #client.send(bytes("*quit*", "utf8"))

            client.close()

            del clients[client]
            broadcast(bytes("%s*quit* has left the chat.*quit*confirme" % name, "utf8"))
            online.remove(name)
            
            
            '''msg=''
            for i in online:
                msg=msg+i
                msg=msg+'@*'
            broadcast(bytes(msg, "utf8"))'''

            break





def broadcast(msg, prefix=""):  # prefix is for name identification.

    """Broadcasts a message to all the clients."""



    for sock in clients:

        sock.send(bytes(prefix, "utf8")+msg)


def chosen_cast(msg, prefix=""):
    global clients
    key_list = list(clients.keys()) 
    val_list = list(clients.values())
    temp_clients_list=[]
    for i in sender_list:
        temp_clients_list.append(key_list[val_list.index(i)])
        
    for sock in temp_clients_list:

        sock.send(bytes(prefix, "utf8")+msg)
    
        

clients = {}

addresses = {}



HOST = ''

PORT = 33300

BUFSIZ = 1024

ADDR = (HOST, PORT)



SERVER = socket(AF_INET, SOCK_STREAM)

SERVER.bind(ADDR)



if __name__ == "__main__":

    SERVER.listen(5)

    print("Waiting for connection...")

    ACCEPT_THREAD = Thread(target=accept_incoming_connections)

    ACCEPT_THREAD.start()

    ACCEPT_THREAD.join()

    SERVER.close()
