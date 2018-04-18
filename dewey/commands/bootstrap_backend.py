import os
import json
import requests
import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        puts("Bootstrapping backend...", newline=False)
        subprocess.call("cd ../backend && docker-compose up -d --no-recreate", shell=True)
        puts(" done.")
        puts("export SIDEBAR_API_URL=%s" % self.brain.api_url)

    def post_default(self, *args, **kwargs):
        pass