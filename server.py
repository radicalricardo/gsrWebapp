import socket
import subprocess

services = ['dhcp', 'dns', 'haproxy', 'nfs', 'snmp-daemon']

"""
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
"""


def serviceChecker(name):
    p = subprocess.Popen(["systemctl", "is-active", name], stdout=subprocess.PIPE)
    (output, err) = p.communicate()
    output = output.decode('utf-8')
    return output


def getInfo():
    for i in range(len(services)):
        print(serviceChecker(services[i]))


if __name__ == '__main__':
    getInfo()
