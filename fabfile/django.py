from fabric.api import env, run, require
from fabric.operations import prompt
from common import virtualenv, _verify_aws_keys_are_set


def _verify_migration_app_is_set():
    if not 'schemamigration_app' in env:
        env.schemamigration_app = prompt('App name for Schema migration (empty for all):', default='')


def _verify_migration_initial_is_set():
    if not 'schemamigration_initial' in env:
        env.schemamigration_initial = prompt('Initial? [y|n]:', default='n')


def migrate():
    # if app == '', south will look for all migrations in all apps
    _verify_migration_app_is_set()
    with virtualenv():
        run('python manage.py migrate {} --settings={}'.format(env.schemamigration_app, env.settings_file))


def schemamigration():
    initial = ''
    _verify_migration_app_is_set()
    _verify_migration_initial_is_set()
    app = env.schemamigration_app
    initial = '--initial' if env.schemamigration_initial == 'y' else ''
    with virtualenv():
        run('python manage.py schemamigration {initial} {app} --settings={settings}'.format(initial=initial,
                                                                                            app=app, settings=env.settings_file))


def django_shell():
    with virtualenv():
        run('python manage.py shell --settings={}'.format(env.settings_file))


def collectstatic():
    _verify_aws_keys_are_set()
    require('aws_access_key_id', 'aws_secret_access_key')
    with virtualenv():
        run('python manage.py collectstatic --settings={}'.format(env.settings_file))


def syncdb():
    with virtualenv():
        run('python manage.py syncdb --noinput --settings={}'.format(env.settings_file))

def createsuperuser():
    with virtualenv():
        run('python manage.py createsuperuser --settings={}'.format(env.settings_file))


def runserver():
    with virtualenv():
        run('python manage.py runserver [::]:8000 --settings={}'.format(env.settings_file))
