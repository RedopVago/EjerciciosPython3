import socket as s
from threading import Thread


class ServidorUDP:
    __server_socket = None

    __sndPktCount = 0
    __rcvPktCount = 0

    ## [[(ip, puerto), mensaje]]
    __packetQueue = []

    ## [[(ip, puerto), rcvPkts, sndPkts], ...]
    __clientes = []
    __processing = False

    __salir = False

    def __init__(self, puerto):
        self.__server_socket = s.socket()
        self.__server_socket.bind(('', puerto))

        while not self.__salir:
            rcv, addrs = self.recibir()

            self.__packetQueue.append([addrs, rcv])

            if not self.__processing:
                tmp = Thread(target=self.procesarPaquete)
                tmp.start()

        self.__server_socket.close()

        ### Mostrar estadisticas

    def enviar(self, mensaje, addr):
        self.__sndPktCount += 1
        print(f'({addr})[SND:{self.__sndPktCount}] {mensaje}')
        self.__server_socket.sendto(mensaje.encode(), addr)

    def recibir(self):
        data, addr = self.__server_socket.recvfrom(1024)
        self.__rcvPktCount += 1
        return data.decode(), addr

    def procesarPaquete(self):

        self.__processing = True

        while len(self.__clientes) > 0:
            addr, rcv = self.__packetQueue.pop(0)

            index = 0

            for index, c in enumerate(self.__clientes):
                if addr == c[0]:
                    self.__clientes[index][1] += 1
                else:
                    self.__clientes.append([addr, 0, 0])

            if rcv == 'Quit':
                msg = f'({addr})[RCV: {self.__rcvPktCount}]: {rcv}'
                self.__salir = True
            else:
                msg = f'{addr}[RCV: {self.__rcvPktCount}]: {rcv}'

            self.enviar(msg, addr)
            self.__clientes[index][2] += 1

        self.__processing = False
