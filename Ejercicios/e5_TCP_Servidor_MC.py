import socket as s
from threading import Thread


class ServidorTCP:

    __sndPktCount = 0
    __rcvPktCount = 0

    ## [[thread, (ip, puerto), rcvPkts, sndPkts], ...]
    __clientes = []
    __clientesCount = 0

    __exit = False

    def __init__(self, puerto):
        self.__server_socket = s.socket()
        self.__server_socket.bind(('', puerto))
        self.__server_socket.listen()

        while not self.__exit:
            cliente_socket, cliente_addr = self.__server_socket.accept()
            self.__clientesCount += 1
            tmp = Thread(target=self.atenderCliente, args=(self.__clientesCount, cliente_socket, cliente_addr))
            tmp.start()
            self.__clientes.append([tmp, cliente_addr, 0, 0])

    def enviar(self, cliente_socket, mensaje):
        cliente_socket.send(mensaje.encode())

    def recibir(self, cliente_socket):
        return cliente_socket.recv(1024).decode()

    def atenderCliente(self, numero, cliente_socket, cliente_addr):

        salir = False

        while not salir:
            rcv = self.recibir()
            self.__clientes[numero][2] += 1

            if rcv == 'Quit':
                msg = f'({cliente_addr})[RCV: {self.__clientes[numero][2]}]: {rcv}. Cerrando socket ...'
                salir = True
                # self.__clientes.pop(numero)
            else:
                msg = f'({cliente_addr})[RCV: {self.__clientes[numero][2]}]: {rcv}'

            self.enviar(msg)
            self.__clientes[numero][3] += 1
            print(f'({cliente_addr})[SND:{self.__clientes[numero][3]}] {msg}')

        cliente_socket.close()


