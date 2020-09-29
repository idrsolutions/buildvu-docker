#!/usr/bin/python3
import os
import subprocess
from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATE_DIRECTORY = 'templates'


def generate_configs():
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIRECTORY), autoescape=select_autoescape(['xml']))
    for template_name in os.listdir(TEMPLATE_DIRECTORY):
        t = env.get_template(template_name)
        with open('conf/' + template_name, 'w') as conf:
            conf.write(t.render(https_enabled=ssl_certificates_provided(), auth_enabled=auth_credentials_provided()))


def war_exists():
    return os.path.isfile('/usr/local/tomcat/webapps/ROOT.war')


def ssl_certificates_provided():
    ssl_dir = '/opt/ssl/'
    ssl_files = [ssl_dir + filename for filename in ['certificate.crt', 'private.key', 'ca_bundle.crt']]
    return all(map(os.path.isfile, ssl_files))


def auth_credentials_provided():
    return all(x in os.environ for x in ['ACCESS_USERNAME', 'ACCESS_PASSWORD'])


if war_exists():
    generate_configs()
    try:
        subprocess.run(['catalina.sh', 'run'], stdout=subprocess.PIPE, universal_newlines=True)
    except KeyboardInterrupt:
        exit()
else:
    print('Error: BuildVu WAR file is missing.')
    print('Please mount your BuildVu Microservice, details can be found at the following link.')
    print('https://docs.idrsolutions.com/buildvu/docker-deployment/')
    exit(1)


