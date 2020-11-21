import subprocess

services = ['bind9', 'isc-dhcp-server', 'nfs-kernel-server', 'haproxy', 'snmpd', 'tomcat7']


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
