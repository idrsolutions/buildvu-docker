#!/usr/bin/python3
import os
import subprocess
import random
import string


def war_exists():
    return os.path.isfile('/usr/local/tomcat/webapps/ROOT.war')


def ssl_certificates_provided():
    return os.path.isdir('/opt/ssl') and os.path.isfile('/opt/ssl/server.crt') and os.path.isfile('/opt/ssl/server.key')


if ssl_certificates_provided():
    os.rename('/usr/local/tomcat/conf/web.xml', '/usr/local/tomcat/conf/http-web.xml')
    os.rename('/usr/local/tomcat/conf/https-web.xml', '/usr/local/tomcat/conf/web.xml')
    os.rename('/usr/local/tomcat/conf/server.xml', '/usr/local/tomcat/conf/http-server.xml')
    os.rename('/usr/local/tomcat/conf/https-server.xml', '/usr/local/tomcat/conf/server.xml')


if 'BUILDVU_USER' not in os.environ:
    os.environ['BUILDVU_USER'] = 'buildvu'
    print('BUILDVU_USER not supplied. Using default username: ' + os.environ['BUILDVU_USER'])

if 'BUILDVU_PASSWORD' not in os.environ:
    os.environ['BUILDVU_PASSWORD'] = ''.join(random.choice(string.ascii_letters) for i in range(10))
    print('BUILDVU_PASSWORD not supplied. Using generated password: ' + os.environ['BUILDVU_PASSWORD'])


if war_exists():
    try:
        subprocess.run(['catalina.sh', 'run'], stdout=subprocess.PIPE, universal_newlines=True)
    except KeyboardInterrupt:
        exit()
else:
    print('Error: BuildVu WAR file is missing. Please mount your BuildVu Microservice, example shown below')
    print('docker run -p 80:80 \\')
    print('--mount "source=/PATH/TO/buildvu-microservice.war,target=/usr/local/tomcat/webapps/ROOT.war,type=bind" \\')
    print('idrsolutions/buildvu')
    exit(1)


