import socket

def server_program():
    # get the hostname
    host = socket.gethostname()

    # initiate port no above 1024
    port = 5000  

    # get instance
    server_socket = socket.socket() 
 
    # look closely - the bind() function takes tuple as argument
    # bind host address and port together
    server_socket.bind((host, port))  

    # configure how many clients the server can listen to simultaneously
    server_socket.listen(2)
    print("Waiting for connection")
    # accept new connection
    conn, address = server_socket.accept()  
    print("Connection from: " + str(address))
    while True:
        # receive data stream - it won't accept a data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received, break out of loop
            break
        print("from connected user: " + str(data))
        data = input(' -> ')

        # send data to the client
        conn.send(data.encode())  

    # close the connection
    conn.close()  

if __name__ == '__main__':
    server_program()
