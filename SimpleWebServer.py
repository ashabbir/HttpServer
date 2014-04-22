#Ahmed Shabbir POLY ID 0504100
#CN 6843
#HTTP Web server : Assignment 1
from socket import *
  
serverSocket = socket(AF_INET, SOCK_STREAM) 
#Prepare a sever socket 

#fill in start
PORT = 1280
IP = "localhost"
MSG200 = "http/1.1 200 OK\r\n\r\n"
MSG404 = "http/1.1 404 Not Found\r\n\r\n"
MSG500 = "http/1.1 500 Internal Server Error\r\n\r\n"

serverSocket.bind((IP,PORT)) 
print "server started - IP: {0}, PORT:{1}".format(IP,PORT)

serverSocket.listen(1) 
#fill in end
while True: 
    #Establish the connection 
      
    print 'Ready to serve...'
    connectionSocket,addr = serverSocket.accept() 
    print 'Received message from ' + str(addr)
    try: 
        message =  connectionSocket.recv(1024)          
        print message
        filename = message.split()[1] 
        f = open(filename[1:]) 
        outputdata = f.read() 

        #Send one HTTP header line into socket 
        connectionSocket.send(MSG200) 
        print MSG200
        
        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i]) 
        
    except IOError as ioe: 
        #Send response message for file not found 
        connectionSocket.send(MSG404) 
        print str(ioe)
        #Close client socket 
        connectionSocket.close() 
    except Exception as e:
        #internal server error
        connectionSocket.send(MSG404) 
        print str(e)
        connectionSocket.close()
        
    finally:
        #close clinet socket on finally
        connectionSocket.close() 
    
    
        
serverSocket.close() 