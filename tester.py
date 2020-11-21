import subprocess
import os

services = ['bind9', 'dhcpd', 'nfs-kernel-server', 'haproxy', 'snmpd', 'tomcat7']


def serviceChecker(name):
    output = os.system('service ' + name + ' status' + ' >/dev/null 2>&1')
    return output


def getInfo():
    for i in range(len(services)):
        print(services[i] + ' status: ' + str(serviceChecker(services[i])))


if __name__ == '__main__':
    getInfo()
