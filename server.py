#!/bin/python3

import socket
import threading
from datetime import datetime
HEADER = 64
PORT = 6040
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
DISCONNECT_MSG = "/exit"
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
messages = []
addresses = []
cons = []
activeusers = []
userconn = {}
helpmessage="Type /msg {name} to send a private message,type /ppl to list the users active in room \n"
def sendmessages(conn,sender_conn,sender_addr,msg,time):
    for client in conn:
        if client != sender_conn:
            client.send(f"{sender_addr}:{msg} \n{time}".encode(FORMAT))
def commands(conn,msg,username):
    if "/help" in msg:
        conn.send(helpmessage.encode(FORMAT))
    if "/ppl" in msg:
        conn.send("Active Users \n".encode(FORMAT))
        for i in activeusers:
            conn.send(f"{i} \n".encode(FORMAT))
    if "/msg" in msg:
        msg=msg.split()
        reciever=msg[1]
        reciever=userconn[reciever]
        msg.pop(0)
        msg.pop(0)
        msg=" ".join(msg)
        reciever.send(f"Private message from {username}: {msg}".encode(FORMAT))
def history(conn):
    msgnum=len(messages)
    conn.send("\n------------------------------------------------- \n".encode(FORMAT))
    conn.send(f"        Previous {msgnum} messages                 \n ".encode(FORMAT))
    for j in messages:
        conn.send(f"\n{j[0]}:{j[1]}\n{j[2]}\n".encode(FORMAT))
    conn.send("\n_________________________________________________\n".encode(FORMAT))
def handleclient(conn,addr):
    print(f"NEW CONNECTION BY {addr}")
    connected = True
    usernameset=False
    username=" "
    while connected:
        now = datetime.now().strftime("%H:%M:%S %p")
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)   
            print(f"{addr}:{msg}")
            if usernameset==False:
                username=msg
                messages.append([username,"joined",now])
                activeusers.append(username)
                usernameset=True
                now+="\n"
                sendmessages(cons,conn,username,"joined",now)
                history(conn)
                userconn[username]=conn
            elif msg == DISCONNECT_MSG: 
                activeusers.remove(username)
                connected = False
                sendmessages(cons,conn,username,"left",now) 
            elif connected == True:
                messages.append([username,msg,now])
                if "/" in msg:
                    commands(conn,msg,username)
                else:
                    sendmessages(cons,conn,username,msg,now)
    conn.close()
def start():
    server.listen()
    print(f"Listening on {SERVER}")
    while True:
        conn,addr = server.accept()
        cons.append(conn)
        addresses.append(addr)
        thread1 = threading.Thread(target=handleclient,args=(conn,addr))
        thread1.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")



print("Starting server...")
start()





