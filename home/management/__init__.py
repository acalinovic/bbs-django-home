import os
import subprocess
import sys
from pathlib import Path

from django.conf import settings

HOME_CONFIG_CONST = {
    'APACHE_ROOT_DIR': None,
    'APACHE_CONF_DIR': None,
    'APACHE_MODULES_DIR': None,
    'APACHE_V_HOSTS_DIR': None,
    'PROJECT_ROOT': None,
    'PROJECT_SETTINGS_FILE': None,
    'PROJECT_URLS_ROOT_FILE': None,
}

if settings.configured:
    if settings.ROOT_URLCONF:
        HOME_CONFIG_CONST['PROJECT_ROOT'] = settings.ROOT_URLCONF.split('.')[0]

candidate_path = os.path.join(settings.BASE_DIR, HOME_CONFIG_CONST['PROJECT_ROOT'], 'settings.py')
if os.path.exists(candidate_path):
    HOME_CONFIG_CONST['PROJECT_SETTINGS_FILE'] = candidate_path

candidate_path = os.path.join(settings.BASE_DIR, HOME_CONFIG_CONST['PROJECT_ROOT'], 'urls.py')
if os.path.exists(candidate_path):
    HOME_CONFIG_CONST['PROJECT_URLS_ROOT_FILE'] = candidate_path


with subprocess.Popen(['which', 'apache2'], stdout=subprocess.PIPE) as proc:
    HOME_CONFIG_CONST['APACHE_ROOT_DIR'] = proc.stdout.read().decode().rstrip()

if HOME_CONFIG_CONST.get('APACHE_ROOT_DIR'):
    try:
        HOME_CONFIG_CONST['APACHE_V_HOSTS_DIR'] = str(Path('/etc/apache2/sites-available').resolve(strict=True).absolute())
        HOME_CONFIG_CONST['APACHE_CONF_DIR'] = str(Path('/etc/apache2/conf-available').resolve(strict=True).absolute())
        HOME_CONFIG_CONST['APACHE_MODULES_DIR'] = str(Path('/etc/apache2/mods-available').resolve(strict=True).absolute())
    except FileNotFoundError as e:
        print(e)

for const, value in HOME_CONFIG_CONST.items():
    try:
        # sys.stdout.write(f'{const}={value}\n')
        os.environ[const] = value
    except TypeError as e:
        print(e, f'Value not set for {const}')

print('---end of init---')
