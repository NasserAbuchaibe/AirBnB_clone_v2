#!/usr/bin/python3
""" ok """
from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
from fabric.api import *
import os.path

env.hosts = ['35.229.74.86', '35.231.88.30']


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """transfer files"""
    if os.path.isfile(archive_path):
        pre_path = archive_path.split("/")[1]
        put(archive_path, "/tmp/")
        pathl = "/tmp/" + pre_path
        pathr = "/data/web_static/releases/" + pre_path.split(".")[0]
        sudo("mkdir -p {:s}".format(pathr))
        sudo("tar -xzf {:s} -C {:s}".format(pathl, pathr))
        sudo("rm {:s}".format(pathl))
        pathm = pathr + "/web_static/*"
        pathd = pathr + "/web_static/"
        sudo("mv {:s} {:s}".format(pathm, pathr))
        sudo("rm -rf {:s}".format(pathd))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {:s} /data/web_static/current".format(pathr))
        print("New version deployed!")
        return True
    else:
        return False


def deploy():
    """ok"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
