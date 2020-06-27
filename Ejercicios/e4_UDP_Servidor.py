import socket as s


class ServidorUDP:
    __server_socket = None

    __sndPktCount = 0
    __rcvPktCount = 0

    def __init__(self, puerto):
        self.__server_socket = s.socket()
        self.__server_socket.bind(('', puerto))

        salir = False

        while not salir:
            rcv, addrs = self.recibir()

            if rcv == 'Quit':
                msg = f'[RCV: {self.__rcvPktCount}]: "{rcv}" from {addrs}. Cerrando socket ...'
                salir = True
            else:
                msg = f'[RCV: {self.__rcvPktCount}]: "{rcv}" from {addrs}'

            self.enviar(msg, addrs)

        self.__server_socket.close()

    def enviar(self, mensaje, addr):
        self.__sndPktCount += 1
        print(f'[SND:{self.__sndPktCount}] {mensaje}')
        self.__server_socket.sendto(mensaje.encode(), addr)

    def recibir(self):
        data, addr = self.__server_socket.recvfrom(1024)
        self.__rcvPktCount += 1
        return data.decode(), addr



