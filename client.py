#!/bin/python3
import socket
import threading

HEADER = 64
PORT = 6040
FORMAT = 'utf-8'
DISCONNECTED_MSG = "/exit"
SERVER = "127.0.1.1"
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
def recieve():
    while True:
        try:
            msg = client.recv(2048).decode(FORMAT)
            print(msg)
        except:
            print("disconnected from server")
            client.close()
            break
receive_thread = threading.Thread(target=recieve)
def send(msg):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length+=b' '*(HEADER-len(send_length))
        client.send(send_length)
        client.send(message)
        if msg == "/exit":
            client.close()
print("------------------------------------------------------------------------")
print("|                     SOCKET TEXTING PROGRAM                           |")
print("________________________________________________________________________")
print("\n Type /exit to disconnect and exit, type /help for list of commands \n")
username=input("Enter your username:")
send(username)
def run():
    a = "y"
    while a!="/exit":
        a=input("")
        send(a)

send_thread = threading.Thread(target=run)
receive_thread.start()
send_thread.start()


