#!/usr/bin/python3
""" comentario """
from fabric.api import *
from datetime import datetime


def do_pack():
    """ Returns archive path if archive was generated """
    local("mkdir -p versions/")
    now = datetime.now()
    date_time = now.strftime("%Y%m%d%H%M%S")
    name = "versions/web_static_" + date_time
    try:
        local("tar -cvzf " + name + ".tgz web_static")
        return "{}.tgz".format(name)
    except:
        return None
