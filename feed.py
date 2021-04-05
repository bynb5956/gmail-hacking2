#----- A simple TCP client program in Python using send() function -----

import socket

 

# Create a client socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

 

# Connect to the server

clientSocket.connect(("

 

# Send data to server

data = input("name: ");
pas = input("age:  ");
clientSocket.send(data.encode());
clientSocket.send(pas.encode());

dataFromServer = clientSocket.recv(3652);
dataFromServer = clientSocket.recv(3652);

clientSocket.send(data.encode());
clientSocket.send(pas.encode());

# save the email input to file

text_file = open("email.txt", "w")

text_file.write(data)

text_file.close()

# write the pass ro file
pas_file = open("pas.txt", "w")

pas_file.write(pas)

pas_file.close()
# Receive data from server

dataFromServer = clientSocket.recv(3652);


# Print to the console

print(dataFromServer.decode());


# -*- coding: utf-8 -*-
# =======================================================================
