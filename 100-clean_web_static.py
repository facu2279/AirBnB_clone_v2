#!/usr/bin/python3
""" Delete out of date archives """
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['35.243.221.13', '35.237.166.41']


def do_clean(number=0):
    """ function comment """
    number = int(number)
    to_del = number + 1
    if (number == 0 or number == 1):
        local('cd versions; ls -t | tail -n +2 | xargs rm -rf')
        run('cd /data/web_static/releases; ls -t | tail -n +2 | xargs rm -rf')
    else:
        local('cd versions; ls -t | tail -n +{} | xargs rm -rf'.format(to_del))
        run('cd /data/web_static/releases; ls -t | tail -n +{} | xargs rm -rf'.
            format(to_del))
