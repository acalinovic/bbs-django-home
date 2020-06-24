DEBUG_BLOCK = """
if DEBUG:
    INTERNAL_IPS = [
        '127.0.0.1',
        ]
    MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware', ] + MIDDLEWARE
    INSTALLED_APPS = ['debug_toolbar', ] + INSTALLED_APPS
"""

CONTEXT_P_BLOCK = """
TEMPLATES[0]['OPTIONS']['context_processors'] = TEMPLATES[0]['OPTIONS']['context_processors'] + ['home.processors.app_menus']
"""

VIRTUAL_HOST_BLOCK = f'''
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
