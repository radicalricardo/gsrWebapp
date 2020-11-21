import subprocess
import os

services = ['dhcp', 'dns', 'haproxy', 'nfs', 'snmp-daemon']


def serviceChecker(name):
    output = os.system('service ' + name + ' status')
    return output


def getInfo():
    for i in range(len(services)):
        print(serviceChecker(services[i]))


if __name__ == '__main__':
    getInfo()
