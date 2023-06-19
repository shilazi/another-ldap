import os

'''
    https://docs.gunicorn.org/en/stable/settings.html#config
    https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py
'''
wsgi_app = 'main:app'
bind = '0.0.0.0:9000'
workers = 4
worker_class = 'gevent'
name = 'aldap'
proc_name = 'aldap'
proxy_protocol = True
proxy_allow_ips = '*'

chdir = os.getenv('HOME', '/aldap')
loglevel = str.lower(os.getenv('LOG_LEVEL', 'info'))

'''
    https://stackoverflow.com/questions/18967441/add-a-prefix-to-all-flask-routes/36033627#36033627
    https://gist.github.com/Larivact/1ee3bad0e53b2e2c4e40
'''
sub_path = os.getenv('SCRIPT_NAME', '')
# will cause an endless loop
if sub_path == '/':
    sub_path = ''
raw_env = [f"SCRIPT_NAME={sub_path}"]

''' debug this conf.py '''
# check_config = True
# print_config = True

'''
https://docs.gunicorn.org/en/stable/settings.html#on-starting
https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies#restrict_access_to_cookies
https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies#define_where_cookies_are_sent
'''
def on_starting(server):
    if not os.getenv('COOKIE_DOMAIN'):
        server.log.error('Working as expected, should set `COOKIE_DOMAIN` first, such as: `.example.org`,'
                         ' and should serving use domain name meanwhile, such as: `aldap.example.org`.')
        raise SystemExit

    if not eval(os.getenv('COOKIE_SECURE', 'True')):
        server.log.warning('Production should set `COOKIE_SECURE` to `True`.')

    server.log.info(f"Serving with:\n"
                    f"    BIND: {bind}\n"
                    f"    SCRIPT_NAME: {sub_path}\n"
                    f"    COOKIE_SECURE: {os.getenv('COOKIE_SECURE', 'True')}\n"
                    f"    COOKIE_DOMAIN: {os.getenv('COOKIE_DOMAIN')}")
