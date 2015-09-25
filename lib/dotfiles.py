"""
Public API that modules can use
"""

import util
import sys

from subprocess import Popen, PIPE

class Module:
    default_dest = "~/"
    overriden_dests = {}

    def install(self):
        """This method is called before the files within a module are copied over
        It should "yield" progress messsages
        """
        return []

    def post_install(self):
        """This is called after the "install" method is called and files are copied over
        Like "install", it should "yield" some messages about its installation progress
        """
        return []

def message(message):
    for line in message.split("\n"):
        if line != "":
            print(util.timestamp(line))

def process(cmd):
    with Popen(cmd, stdout=PIPE, stdin=sys.stdin, shell=True) as proc:
        for line in proc.stdout:
            message(line.decode("utf-8"))
