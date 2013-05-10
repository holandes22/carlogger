import os
from fabric.operations import prompt
from fabric.context_managers import prefix
from fabric.api import env, local, run, cd, require
from contextlib import contextmanager


@contextmanager
def virtualenv():
    _verify_settings_type_is_set()
    _verify_aws_keys_are_set()
    require('settings_file')
    with cd('/vagrant'):
        eid = 'export AWS_ACCESS_KEY_ID={}'.format(env.aws_access_key_id)
        ekey = 'export AWS_SECRET_ACCESS_KEY={}'.format(env.aws_secret_access_key)
        with prefix('source /home/vagrant/virtualenvs/carlogger/bin/activate && export SECRET_KEY=dev && {} && {}'.format(eid, ekey)):
            yield


def vagrant():
    # change from the default user to 'vagrant'
    env.user = 'vagrant'
    # connect to the port-forwarded ssh
    hostname = local('vagrant ssh-config | grep HostName', capture=True)
    port = local('vagrant ssh-config | grep Port', capture=True)
    env.hosts = ['{0}:{1}'.format(hostname.split()[1], port.split()[1]), ]

    # use vagrant ssh key
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1].strip('"')


def _verify_settings_type_is_set():
    if not 'settings_type' in env:
        env.settings_type = prompt("Settings type to [prod|dev]", default='dev')
    if env.settings_type == 'dev':
        env.settings_file = 'carlogger.settings.dev'
    else:
        env.settings_file = 'carlogger.settings.prod'

def _verify_aws_keys_are_set():
    if not 'aws_access_key_id' in env:
        env.aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
    if not 'aws_secret_access_key' in env:
        env.aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
