# coding: utf-8
import socket
import ssl
import string
import sched
import requests
from parenthesis import matchParenthesis

server = ""
port =  
channel = ""
botname = "Per"
cmdprefix = ""

def rawSend(data):
    ircsock.send(data + "\r\n")
    
def sendMessage(recipient, message):
    if message and isinstance(message, tuple):
        for i in message:
            rawSend("PRIVMSG " + recipient + " :" + i + "\r\n")
    elif message:
        rawSend("PRIVMSG " + recipient + " :" + message + "\r\n")
        
        
def joinchan(channel):
    rawSend("JOIN " + channel + "\r\n")

def parseMessage(message):
    prefix = ''
    sender = ''
    chan = ''
    messageType = ''
    text = ""
    command = ""
    if not message:
        pass
    if(message[0] == ":"):
        prefix,message = message[1:].split(" ",1)
        sender = prefix.split("!",1)[0]
        messageType, message = message.split(" ", 1)
        chan, message = message.split(" ", 1)
        text = message[1:]
        if(text[0] == cmdprefix):
            try:
                command, text = text.split(" ",1)
            except Exception as e:
                print(e)
                command = text

    ret = {"sender": sender,
            "messageType": messageType,
            "chan": chan,
            "command":command,
            "text": text}
    return ret


ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock = ssl.wrap_socket(ircsock)
ircsock.connect((server, 6697))
rawSend("USER " + botname + " " + botname + " " + botname + " " + botname + "\n")
rawSend("NICK " + botname + "\n")
joinchan(channel)

while 1:
    ircmessage = ircsock.recv(2048)
    
    if "ING" in ircmessage:
        pong = ircmessage[6:].split("\r")[0]
        if(pong != "irc.velox.pw"):
            rawSend("PONG " + pong)
            joinchan(channel)
        else:
            rawSend("PONG")
        continue 

    elif(ircmessage != ""):
        msg = parseMessage(ircmessage)
        paran = matchParenthesis(msg["text"])
        if not paran == "":
            try:
                sendMessage(channel, paran)
            except Exception as e:
                print(e)
        continue
