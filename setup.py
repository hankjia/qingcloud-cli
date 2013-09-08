# coding:utf-8

import os
import platform
from setuptools import setup, find_packages

config_sample = '''
qy_access_key_id: 'QINGCLOUDACCESSKEYID'
qy_secret_access_key: 'QINGCLOUDSECRETACCESSKEYEXAMPLE'
zone: 'pek1'
'''

def prepare_config_file():
    config_file = os.path.expanduser('~/.qingcloud/config.yaml')
    if os.path.exists(config_file):
        return

    d = os.path.dirname(config_file)
    if not os.path.exists(d):
        os.makedirs(d)

    with open(config_file, 'w') as fd:
        fd.write(config_sample)

def setup_qingcloud_completer():
    # only support linux
    if platform.system().lower() == 'windows':
        return

    cmd = 'complete -C qingcloud_completer qingcloud'
    complete_file = '/etc/bash_completion.d/qingcloud-cli'
    if not os.path.exists(os.path.dirname(complete_file)):
        with open(os.path.expanduser('~/.bash_profile'), 'a') as fd:
            fd.write('\n\n# QingCloud CLI\n%s\n' % cmd)
    else:
        with open((complete_file), 'w') as fd:
            fd.write(cmd)


setup(
    name = 'qingcloud-cli',
    version = '0.6.3',
    description = 'Command Line Interface for QingCloud.',
    long_description = open('README.rst', 'rb').read().decode('utf-8'),
    keywords = 'qingcloud iaas cli',
    author = 'Yunify Team',
    author_email = 'simon@yunify.com',
    url = 'https://docs.qingcloud.com/cli/',
    scripts=['bin/qingcloud', 'bin/qingcloud_completer', 'bin/qingcloud.cmd'],
    packages = find_packages('.'),
    package_dir = {'qingcloud-cli': 'qingcloud'},
    include_package_data = True,
    install_requires = [
        'argparse>=1.1',
        'PyYAML>=3.1',
    ]
)

prepare_config_file()

setup_qingcloud_completer()
