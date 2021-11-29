import socket
import os
from _thread import *


class Game():
    def __init__():
        self.players = list()

class Client():
    def __init__(self, socket, ip_address):
        self.socket = socket
        self.ip_address = ip_address
        self.pseudo = ""
        self.board_pos = 0

    def __str__(self):
        return "client ({0}): {1}".format(self.pseudo, self.ip_address)


    def receive(self, size):
        return self.socket.recv(size)

    def send(self, data):
        message = str(data)
        self.socket.send(message.encode('ascii'))

    def setPseudo(self, new_pseudo):
        self.pseudo = new_pseudo

# Class to define the network and its operations:
class Server():

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 1233

        self.server_socket = socket.socket()

        self.client_connexions = []
        self.clients = list()
        self.client_count = 0

        self.data = 0

    # Function to launch the server
    def start(self):
        try:
            self.server_socket.bind((self.host, self.port))
        except socket.error as e:
            print(str(e))

        self.server_socket.listen(5)

    def waiting_for_clients(self, max_clients):
        # Until we have all clients connected:
        while self.client_count < max_clients:
            # We accept clients
            temp_client, temp_address = self.server_socket.accept()

            # We add the new client
            self.clients.append(Client(temp_client, temp_address[0]))
            print("New connection: {0} on port {1}".format(temp_address[0], str(temp_address[1])))
            self.client_count += 1

            # We send back a message
            #self.client_connexions[self.client_count - 1][0].send(str.encode('Connected to the Server'))
            
    def send_all(self, data):
        for client in self.clients:
            message = str(data)
            client.send(message.encode('ascii'))

    def send(self, data, pseudo):
        for client in self.clients:
            if client.pseudo == pseudo:
                client.send(message.encode('ascii'))

    def receive(self, pseudo):
        # If we want to receive data from one client, we specify which one it is
        # We wait to receive data
        for client in self.clients:
            if client.pseudo == pseudo:
                temp_data = client.receive(1024)

                # We decode the data
                temp_data = temp_data.decode('ascii')

                # We take out the brackets
                temp_data = temp_data[1:len(temp_data) - 1]
                # We split it
                temp_data = temp_data.split(", ")

                for values in range(0, len(temp_data)):
                    # Then convert each parameters as an integer
                    temp_data[values] = int(temp_data[values])

        return temp_data
        
def main():
    CLIENT_COUNT = 2
    server = Server()

    print("Server starting...")
    server.start()                              # start server
    print("Server started.")
    print("Waiting for players to connect...")
    server.waiting_for_clients(CLIENT_COUNT)    # wait for all players to connect
    print(server.clients)

    # get all the players first message (only pseudo)
    data = None
    for client in server.clients:
        data = client.receive(1024)
        data = data.decode('ascii')
        client.setPseudo(str(data))

    print("Connected clients:")
    for client in server.clients:
        print("{0} : {1}".format(client.pseudo, client.ip_address))

    # once all the players are connected we send them the signal to go to the gamescreen
    game_data = list() # lobby loop data format: (pseudo: str, ready: binint) * nb_clients
    ready_count = 0
    while ready_count < 2:# while not every player is ready
        for client in server.clients:
            message = client.receive(1024)
            data = message.decode('ascii')
            if int(data) != 0:
                ready_count +=1
                print("{0} is ready.".format(client.pseudo))

    print("Everybody is ready.")

    # once everybody is ready, notify all
    array = []
    for client in server.clients:
        array.append(client.pseudo)
        array.append(1)

    server.send_all(array)

    # TODO: lobby loop
    #       in game loop
    
    # Main game loop
    running = False
    turn = 1
    game_data = list()
    game_data.append(turn)
    for i in range(CLIENT_COUNT):
        game_data.append(server.clients[i].pseudo)
        game_data.append(server.clients[i].board_pos)

    while running:
        
        # update all clients
        j = 0
        game_data[j] = turn
        for i in range(CLIENT_COUNT):
            game_data[j] = server.clients[i].pseudo
            j+=1
            game_data[j] = server.clients[i].board_pos
            j+=1

        print("Sending ", game_data, "to all clients.")
        server.send_all(game_data)

        # getting data from client who's turn it is
        data = server.client[turn - 1].receive(1024)
        print(data.decode('ascii'))
        # 

        if turn >= CLIENT_COUNT:
            turn = 1

    
    """
    server.send_all(game_stats)
    response = server.receive_data()
    print("one done", game_stats)

    server.send_data(game_stats[0], 0)
    game_stats[0] = network.receive_data(0)
    print("finished", game_stats)

    server.server_socket.close()
    """

    server.server_socket.close()

if __name__ == "__main__":
    main()
