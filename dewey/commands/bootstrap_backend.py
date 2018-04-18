import os
import json
import requests
import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        return "ngrok http 8120 &> /dev/null &"

    def run_command(self, *args, **kwargs):
        puts("Verifying tunnel...", newline=False)
        r = requests.get("http://localhost:4040/api/tunnels")
        j = r.json()
        if "tunnels" in j:
            self.brain.api_url = j["tunnels"][0]["public_url"]
            self.save()
            os.environ["SIDEBAR_API_URL"] = self.brain.api_url
            puts(" found at %s." % self.brain.api_url)

        puts("Bootstrapping backend...", newline=False)
        subprocess.call("cd ../backend && docker-compose up -d --no-recreate", shell=True)
        puts(" done.")

    def post_default(self, *args, **kwargs):
        pass
