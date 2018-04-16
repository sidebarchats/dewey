import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        if self.has_local_override("build"):
            puts("dewey.yml Found.\nRunning build...")
            for c in self.local["build"]:
                print("Running %s" % c)
                subprocess.call(c, shell=True)

    def post_default(self, *args, **kwargs):
        pass
