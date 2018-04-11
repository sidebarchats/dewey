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
            # Use procfile / docker / node detection to spin
            # If procfile
            # Else if docker
            # Else if npm, make sure the docker container is running.
        except KeyboardInterrupt:
            print "\n\nShutting down."


    def post_default(self, *args, **kwargs):
        pass
