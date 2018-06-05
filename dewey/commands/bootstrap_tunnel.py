import os
import json
import requests
import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        return "{ ngrok http 8120 &> /dev/null & } 2>/dev/null"

    def run_command(self, *args, **kwargs):
        puts("Verifying tunnel...", newline=False)
        retries = 0
        while retries < 2:
            r = requests.get("http://localhost:4040/api/tunnels")
            j = r.json()
            if "tunnels" in j:
                try:
                    self.brain.api_url = j["tunnels"][0]["public_url"]
                    self.save()
                    os.environ["SIDEBAR_API_URL"] = self.brain.api_url
                    puts(" found at %s." % self.brain.api_url)

                    if os.path.isfile(".env"):
                        puts("Updating .env file...", newline=False)
                        with open(".env", "r+") as f:
                            contents = f.read()
                            new_contents = ""
                            for l in contents.split("\n"):
                                if "SIDEBAR_API_URL" not in l:
                                    new_contents += "%s\n" % l
                            new_contents += "SIDEBAR_API_URL=%s\n" % self.brain.api_url
                            f.seek(0)
                            f.truncate()
                            f.write(new_contents)
                            puts(" done.")
                    return 
                except:
                    retries += 1

        puts("Failed to set tunnel.  Output: %s" % j)

    def post_default(self, *args, **kwargs):
        if self.brain.api_url:
            return 'export SIDEBAR_API_URL=%s' % self.brain.api_url
        pass
