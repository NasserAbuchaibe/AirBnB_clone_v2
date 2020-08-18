#!/usr/bin/python3
"""ok
"""
from datetime import datetime
from fabric.api import *
import os.path
env.hosts = ['35.229.74.86', '35.231.88.30']


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
        sudo("rm -rf {:s}".format(pathdd))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {:s} /data/web_static/current".format(pathr))
        print("New version deployed!")
        return True
    else:
        return False
