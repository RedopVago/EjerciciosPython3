import socket as s


class ServidorTCP:
    __cliente_socket = None
    __cliente_addr = None

    __sndPktCount = 0
    __rcvPktCount = 0

    def __init__(self, puerto):
        self.__server_socket = s.socket()
        self.__server_socket.bind(('', puerto))
        self.__server_socket.listen()
        (self.__cliente_socket, self.__cliente_addr) = self.__server_socket.accept()

        salir = False

        while not salir:
            rcv = self.recibir()

            if rcv == 'Quit':
                msg = f'[RCV: {self.__rcvPktCount}]: {rcv}. Cerrando socket ...'
                salir = True
            else:
                msg = f'[RCV: {self.__rcvPktCount}]: {rcv}'

            self.enviar(msg)

        self.__cliente_socket.close()

    def enviar(self, mensaje):
        self.__sndPktCount += 1
        print(f'[SND:{self.__sndPktCount}] {mensaje}')
        self.__cliente_socket.send(mensaje.encode())

    def recibir(self):
        r = self.__cliente_socket.recv(1024).decode()
        self.__rcvPktCount += 1
        return r
