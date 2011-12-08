"""
Fabtools recipe to install pystatsd

http://github.com/sivy/py-statsd
"""
import os.path

from fabric.api import *
from fabtools.python import virtualenv
from fabtools import require


@task
def install_pystatsd(target_dir='/opt/graphite', port=8125,
                     graphite_host='localhost', graphite_port=2003):
    """
    Install pystatsd
    """
    require.python.virtualenv(target_dir)
    with virtualenv(target_dir):
        require.python.package('pystatsd', virtualenv=target_dir)

    binary = os.path.join(target_dir, 'bin', 'pystatsd-server')
    options = [
        '--port %s' % port,
        '--graphite-host %s' % graphite_host,
        '--graphite-port %s' % graphite_port,
    ]
    require.supervisor.process('pystatsd',
        command="%s %s" % (binary, ' '.join(options)),
        directory=target_dir,
        user=env.user
        )
