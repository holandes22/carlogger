from fabric.api import env, run
from common import virtualenv


def stopwsgi():
    run('kill `cat /tmp/gunicorn.pid`')


def startwsgi():
    with virtualenv():
        args = '-w 9 -k gevent --max-requests 250 --preload --pid=/tmp/gunicorn.pid'
        run('python manage.py run_gunicorn 0.0.0.0:8000 --settings={} {}'.format(env.settings_file, args))
