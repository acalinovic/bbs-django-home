import errno
import os
import shutil
import subprocess
import sys

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = '''
    firts test
    '''

    def add_arguments(self, parser):
        parser.add_argument(
            '--full',
            action='store_true',
            help='Full setup',
        )
        parser.add_argument(
            '--apache',
            action='store_true',
            help='Apache2 install if not present',
        )
        parser.add_argument(
            '--wsgi',
            action='store_true',
            help='mod-wsgi install if not present',
        )
        parser.add_argument(
            '--modules',
            action='store_true',
            help='Modules install if not present',
        )



    def handle(self, *args, **options):
        """
        'APACHE_ROOT_DIR': Apache2 home,
        'APACHE_CONF_DIR': Apache2 conf-available,
        'APACHE_MODULES_DIR': Apache2 mods-available,
        'APACHE_V_HOSTS_DIR': Apache2 sites-available,
        'PROJECT_ROOT': Current project root app,
        'PROJECT_SETTINGS_FILE': Current project settings file,
        'PROJECT_URLS_ROOT_FILE': Current project urls file,
        """
        p_root_dir, p_settings_file, p_urls_file = None, None, None
        a_root_dir, a_confs_dir, a_mods_dir, a_vhosts_dir = None, None, None, None
        if options['full']:
            self.stdout.write(self.style.SUCCESS('Full mode used'))
            try:
                p_root_dir = os.environ.pop('PROJECT_ROOT')
                p_settings_file = os.environ.pop('PROJECT_SETTINGS_FILE')
                p_urls_file = os.environ.pop('PROJECT_URLS_ROOT_FILE')
                a_root_dir = os.environ.pop('APACHE_ROOT_DIR')
                a_confs_dir = os.environ.pop('APACHE_CONF_DIR')
                a_mods_dir = os.environ.pop('APACHE_MODULES_DIR')
                a_vhosts_dir = os.environ.pop('APACHE_V_HOSTS_DIR')
            except KeyError as e:
                self.stderr.write(e)

            with open(p_settings_file, mode='a') as f:
                try:
                    os.makedirs(os.path.join(settings.BASE_DIR, 'templates'))
                except OSError as e:
                    if e.errno != errno.EEXIST:
                        raise
                try:
                    os.makedirs(os.path.join(settings.BASE_DIR, 'static'))
                except OSError as e:
                    if e.errno != errno.EEXIST:
                        raise
                try:
                    os.makedirs(os.path.join(settings.BASE_DIR, 'media'))
                except OSError as e:
                    if e.errno != errno.EEXIST:
                        raise

                f.write('### automatic bbs setup ###\n')
                if not settings.MEDIA_URL:
                    print('MEDIA_URL not found')
                f.write('MEDIA_URL = \'/media/\'\n')
                if not settings.MEDIA_ROOT:
                    print('MEDIA_ROOT not found')
                f.write('MEDIA_ROOT = \'media\'\n')
                try:
                    import debug_toolbar
                    text = """
if DEBUG:
    INTERNAL_IPS = [
        '127.0.0.1',
        ]
    MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware', ] + MIDDLEWARE
    INSTALLED_APPS = ['debug_toolbar', ] + INSTALLED_APPS
"""
                    f.write(text)
                except ImportError as e:
                    self.stderr.write(e)
                text = """
TEMPLATES[0]['OPTIONS']['context_processors'] = TEMPLATES[0]['OPTIONS']['context_processors'] + ['home.processors.app_menus']
"""
                f.write(text)

                text = '''
INSTALLED_APPS += [
    'bootstrap4',
    'jquery',
    'jquery_ui',
    'fontawesome_5',
]
'''
                f.write(text)

            with open(p_urls_file, mode='a') as f:
                text = '''
try:
    from bbs import settings

    if settings.MEDIA_ROOT:
        from django.conf.urls.static import static

        urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, )

    if settings.DEBUG:
        import debug_toolbar

        urlpatterns = [path('__debug__/', include(debug_toolbar.urls)), ] + urlpatterns
except ModuleNotFoundError:
    pass
'''
                f.write(text)

                group = r'{GROUP}'
                project_name = 'cookbook'
                server_admin = 'boris.acalinovic@gmail.com'
                python_home = f'{settings.BASE_DIR}/bbs-venv'
                python_path = f'{settings.BASE_DIR}'
                site = 'cookbook'
                domain = 'bluebear.be'
                server_name = f'{site}.{domain}'
                data = f'''
<VirtualHost {server_name}:80>
    ServerName {server_name}
    ServerAlias {domain}
    ServerAdmin {server_admin}
    DocumentRoot {settings.BASE_DIR}

    Alias /robots.txt {settings.BASE_DIR}/robots.txt
    Alias /favicon.ico {settings.BASE_DIR}/favicon.ico
    Alias /media/ {settings.BASE_DIR}/media/
    Alias /static/ {settings.BASE_DIR}/static/

    <Directory {settings.BASE_DIR}/media>
        Require all granted
    </Directory>
    <Directory {settings.BASE_DIR}/static>
        Require all granted
    </Directory>
    <Directory {settings.BASE_DIR}>
        Require all granted
    </Directory>

    WSGIDaemonProcess {server_name} python-home={python_home} python-path={python_path}  processes=2 threads=15 display-name=%{group}
    WSGIProcessGroup {server_name}

    WSGIScriptAlias / {settings.BASE_DIR}/{p_root_dir}/wsgi.py
</VirtualHost>
                '''
                target_path = f'{settings.BASE_DIR}/{server_name}.conf'
                if os.path.exists(target_path):
                    os.remove(target_path)
                    # open(target_path, mode='x').close()
                with open(target_path, mode='x') as conf_file:
                    conf_file.write(data)
                try:
                    target = a_vhosts_dir + '/' + server_name + '.conf'
                    print(f'target: {target}')
                    shutil.copy2(target_path, target)
                    os.symlink(src=target_path, dst=os.path.join(a_vhosts_dir.replace('available', 'enabled'), server_name + '.conf'))
                    with subprocess.Popen(['systemctl', 'reload', 'apache2'], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as p:
                        self.stdout.write(p.stdout.read().decode())
                        self.stderr.write(p.stderr.read().decode())

                except PermissionError:
                    self.stderr.write(f'{target} not copied. Probably not ran as root')
        self.stdout.write(self.style.SUCCESS('Successfully installed home in mode FULL'))
