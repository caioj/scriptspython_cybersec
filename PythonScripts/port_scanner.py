import socket

alvo = input("Alvo: ")
portas = [22,80,443,53,21,23,8080]
for porta in portas:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Cria um novo socket usando a família de endereços IPv4 (AF_INET) e o protocolo TCP (SOCK_STREAM)
    sock.settimeout(10)
    resultado = sock.connect_ex((alvo, porta))
    sock.close()
    if (resultado == 0):
        print(porta)