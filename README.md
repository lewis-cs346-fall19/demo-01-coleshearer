Names: Akshith, Cole
Assignment: Lab 1
Purpose: To be able to send a message to a server from a cliet.


Server File:

We first imported socket into the sever file and assigned one to the server
and created an address for the server.

Binding the address was very important.

Using the listen() function we were able to let the server listen

We used a for loop to define the number of times the server accepts messages

Using a try block we recieved the messege from the client and decoded it.

else we closed the socket

And after we encode the message using the encode() method

We send the return messege to the client. 


Client File:

imported the socket library

made a socket object and assigned a hostname to it

Then also assigned the server address to the local client

using a for loop we ask for the user input and send 5 messages.

Then try to print the messege recieved from the server. 
