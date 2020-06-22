import socket as s

cliente = s.socket(s.AF_INET, s.SOCK_DGRAM)


ip = '127.0.0.1'
port = 12345

addr = ip, port

msg = 'Mensaje de cliente'
cliente.sendto(msg.encode(), addr)

data, addr = cliente.recvfrom(1024)

print(f'Recibido: {data} de {addr}')



