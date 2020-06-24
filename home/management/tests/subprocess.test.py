#! /usr/bin/python3
import os
import subprocess
import shutil

# init settings
settings_bckp = '/home/boris/dev/python/bbs-django-cookbook/bbs/settings.bckp.py'
settings_file = '/home/boris/dev/python/bbs-django-cookbook/bbs/settings.py'
urls_bckp = '/home/boris/dev/python/bbs-django-cookbook/bbs/urls.bckp.py'
urls_file = '/home/boris/dev/python/bbs-django-cookbook/bbs/urls.py'
vhost_conf_file = '/etc/apache2/sites-available/cookbook.bluebear.be.conf'
vhost_conf_symlink = '/etc/apache2/sites-enabled/cookbook.bluebear.be.conf'
try:
    os.remove(vhost_conf_symlink)
    os.remove(vhost_conf_file)
except FileNotFoundError:
    print('vhost files already removed')
else:
    print('vhost files removed')
shutil.copy(settings_bckp, settings_file)
shutil.copy(urls_bckp, urls_file)
