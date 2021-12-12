host, port = "127.0.0.1", 25003
import socket
import time

noobArr = []
with open('data.csv') as my_file:
    for line in my_file:
        noobArr.append(line)
print(type(noobArr[0]))


i = 0
        
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

#startPos = [0,0,1] #Vector3   x = 0, y = 0, z = 1
while True:
    time.sleep(0.1) #sleep 0.5 sec
    #startPos[2] +=1 #increase z by one
    posString = noobArr[i]
    print(i)
    if (i>60):
        i=0
    #Converting Vector3 to a string, example "0,0,0"
    print(posString)
    sock.sendall(posString.encode("UTF-8")) #Converting string to Byte, and sending it to C#
    receivedData = sock.recv(1024).decode("UTF-8") #receiveing data in Byte fron C#, and converting it to String
    print(receivedData)