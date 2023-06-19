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
