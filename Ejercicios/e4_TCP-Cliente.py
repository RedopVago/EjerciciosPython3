import socket as s

class ClienteTCP:

    __sock = None
    __sndPktCount = 0
    __rcvPktCount = 0

    def __init__(self, ip, puerto):
        self.__sock = s.socket()
        self.__sock.connect((ip, puerto))

        salir = True

        while not salir:
            print('Escribe un mensaje (Quit para salir):')
            tmp = input()

            self.enviar(tmp.encode())

            rcv = self.recibir()

            if rcv == b'':
                salir = True
                print('Saliendo ...')
            else:
                print(f'[RCV: {self.__rcvPktCount}] {rcv}')

    def enviar(self, mensaje):
        self.__sndPktCount += 1
        print(f'[SND:{self.__sndPktCount}] {mensaje}')
        self.__sock.send(mensaje.encode())

    def recibir(self):
        r = self.__sock.recv(1024).decode()
        self.__rcvPktCount += 1
        return r
