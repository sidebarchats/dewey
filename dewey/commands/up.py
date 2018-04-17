import sys
import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        try:
            if not self.has_local_override("dev"):
                puts("'dev' section in dewey.yml not found.  Not sure how to start this project.")
                # Use procfile / docker / node detection to spin
                # If procfile
                # Else if docker
                # Else if npm, make sure the docker container is running.
        except KeyboardInterrupt:
            print("\n\nShutting down.")

    def post_default(self, *args, **kwargs):
        if self.has_local_override("dev"):
            return " && ".join(self.local["dev"])
