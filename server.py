import socket
import os

SERVICES = ['bind9', 'dhcpd', 'nfs-kernel-server', 'haproxy', 'snmpd', 'tomcat7']
HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected: ', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)


def serviceChecker(name):
    output = os.system('service ' + name + ' status' + ' >/dev/null 2>&1')
    return output


def getInfo():
    for i in range(len(SERVICES)):
        print(SERVICES[i] + ' status: ' + str(serviceChecker(SERVICES[i])))


