from fabric.api import env, run, require
from common import virtualenv


def migrate():
    # if app=='', south will look for all migrations in all apps
    'python manage.py migrate {}'.format('app')


def schemamigration():
    'python manage.py schemamigration --initial {app} --settings={settings}'.format(app='name', settings='name')


def django_shell():
    with virtualenv():
        run('python manage.py shell --settings={}'.format(env.settings_file))


def collectstatic():
    require('aws_access_key_id', 'aws_secret_access_key')
    with virtualenv():
        run('python manage.py collectstatic --settings={}'.format(env.settings_file))


def syncdb():
    with virtualenv():
        run('python manage.py syncdb --noinput --settings={}'.format(env.settings_file))


def runserver():
    with virtualenv():
        run('python manage.py runserver [::]:8000 --settings={}'.format(env.settings_file))
