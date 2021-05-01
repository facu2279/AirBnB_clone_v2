#!/usr/bin/python3
""" comentario """
from fabric.api import *
from datetime import datetime
import os


env.hosts = ['35.243.221.13', '35.237.166.41']


def do_pack():
    """ function comment """
    local("mkdir -p versions/")
    now = datetime.now()
    date_time = now.strftime("%Y%m%d%H%M%S")
    name = "versions/web_static_" + date_time
    try:
        local("tar -cvzf " + name + ".tgz web_static")
        return "{}.tgz".format(name)
    except Exception:
        return None


def do_deploy(archive_path):
    """Fabric script distributes archive to web servers """
    if os.path.exists(archive_path):
        try:
            put(archive_path, "/tmp/")
            """ file_name name of file with .tgz """
            file_name = archive_path.split("/")[1]
            """ file_name2 name of file without .tgz """
            file_name2 = file_name.split(".")[0]
            """ final_name name of path of directory """
            final_name = "/data/web_static/releases/" + file_name2 + "/"
            run("mkdir -p " + final_name)
            run("tar -xzf /tmp/" + file_name + " -C " + final_name)
            run("rm /tmp/" + file_name)
            run("mv " + final_name + "web_static/* " + final_name)
            run("rm -rf " + final_name + "web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s " + final_name + " /data/web_static/current")
            print("New version deployed!")
            return True
        except:
            return False
    else:
        return False


def deploy():
    """ Function comment """
    file_path = do_pack()
    if file_path is None:
        return False
    return do_deploy(file_path)
