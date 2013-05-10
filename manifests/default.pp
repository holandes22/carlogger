Exec { path => '/usr/bin:/bin:/usr/sbin:/sbin' }

exec { "apt-get update": }

$needed_packages = [ "build-essential", "libpq-dev", "libevent-dev"]
$enhancer_packages = [ "git", "vim"]

package { [$needed_packages, $enhancer_packages] : 
    ensure => present,
    require => Exec["apt-get update"],
}

### DB settings ###

class {'postgresql':
    version => '9.1',
}

class {'postgresql::server':
    version => '9.1',
}

pg_user {'vagrant':
    ensure   => present,
    password => 'vagrant',
    createdb   => true,
    createrole => true,
}

pg_database {'carlogger_db':
    ensure   => present,
    owner    => 'vagrant',
    require  => Pg_user['vagrant'],
}

### Python ###

class { 'python':
    version    => 'system',
    dev        => true,
    virtualenv => true,
    gunicorn   => false,
}

python::virtualenv { '/home/vagrant/virtualenvs/carlogger':
  ensure       => present,
  version      => 'system',
  requirements => '/vagrant/requirements.txt',
}

