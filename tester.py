import subprocess
import os

services = ['bind9', 'isc-dhcp-server', 'nfs-kernel-server', 'haproxy', 'snmpd', 'tomcat7']


def serviceChecker(name):
    output = os.system('service ' + name + ' status')
    return output


def getInfo():
    for i in range(len(services)):
        print(serviceChecker(services[i]))


if __name__ == '__main__':
    getInfo()
