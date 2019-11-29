#!/usr/bin/python3
import os
import random
import string
import subprocess
from urllib import parse
from urllib import request
from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATE_DIRECTORY = 'templates'
redownload = 'REDOWNLOAD' in os.environ


def generate_configs():
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIRECTORY), autoescape=select_autoescape(['xml']))
    for template_name in os.listdir(TEMPLATE_DIRECTORY):
        t = env.get_template(template_name)
        with open('conf/' + template_name, 'w') as conf:
            conf.write(t.render(https_enabled=ssl_certificates_provided(), auth_enabled=auth_credentials_provided()))


def download_trial_war():
    print('Downloading BuildVu trial...')
    token = os.environ['TOKEN']
    url = 'https://files.idrsolutions.com/dl/buildvu/trial/buildvu-microservice.war?token=' + token
    with request.urlopen(url) as response:
        handle_response(response)


def download_full_war(url):
    username = os.environ['USERNAME']
    password = os.environ['PASSWORD']
    data = parse.urlencode({'username': username, 'password': password}).encode('ascii')
    with request.urlopen(url, data) as response:
        handle_response(response)


def handle_response(response):
    if response.status == 200:
        with open('/usr/local/tomcat/webapps/ROOT.war', 'wb') as f:
            f.write(response.read())
        print('Download successful')
    else:
        print('Download failed')
        print(response.read().decode())


def download_buildvu():
    print('Downloading BuildVu...')
    download_full_war('https://files.idrsolutions.com/dl/buildvu/full/buildvu-microservice.war')


def download_buildvu_html():
    print('Downloading BuildVu HTML...')
    download_full_war('https://files.idrsolutions.com/dl/buildvu-html/full/buildvu-microservice.war')


def download_buildvu_svg():
    print('Downloading BuildVu SVG...')
    download_full_war('https://files.idrsolutions.com/dl/buildvu-svg/full/buildvu-microservice.war')


def is_trial():
    return 'TOKEN' in os.environ


def is_full():
    return all(x in os.environ for x in ['USERNAME', 'PASSWORD', 'PRODUCT'])


def new_war_required():
    return ('REDOWNLOAD' in os.environ) or not war_exists()


def war_exists():
    return os.path.isfile('/usr/local/tomcat/webapps/ROOT.war')


def ssl_certificates_provided():
    ssl_dir = '/opt/ssl/'
    ssl_files = [ssl_dir + filename for filename in ['certificate.crt', 'private.key', 'ca_bundle.crt']]
    return all(map(os.path.isfile, ssl_files))


def auth_credentials_provided():
    return all(x in os.environ for x in ['BUILDVU_USER', 'BUILDVU_PASSWORD'])


if new_war_required():
    if is_trial() and is_full():
        print('Mixing trial TOKENs and full-version USERNAME/PASSWORD combination is not supported.')
        print('If you have purchased a license, please remove the TOKEN argument to use the full version.')
        print('If you wish to trial BuildVu, please remove any USERNAME, PASSWORD or PRODUCT argument.')
        exit(2)
    elif is_full():
        product = os.environ['PRODUCT'].lower()
        if product == 'buildvu':
            download_buildvu()
        elif product == 'buildvu_html':
            download_buildvu_html()
        elif product == 'buildvu_svg':
            download_buildvu_svg()
        else:
            print('Error: Unrecognised product "' + product + '".')
            print('Valid options are "buildvu", "buildvu_html" or "buildvu_svg.')
            exit(2)
    elif is_trial():
        download_trial_war()
    else:
        print('Please provide a valid trial token or username/password/product combination to download BuildVu')

if war_exists():
    generate_configs()
    try:
        subprocess.run(['catalina.sh', 'run'], stdout=subprocess.PIPE, universal_newlines=True)
    except KeyboardInterrupt:
        exit()
else:
    print('Error: BuildVu WAR file is missing.')
    exit(1)


