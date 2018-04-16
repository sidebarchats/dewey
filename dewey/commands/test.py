import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr



class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        if not self.has_local_override("test"):
            return 'pt'

    def run_command(self, *args, **kwargs):
        if self.has_local_override("test"):
            puts("dewey.yml Found.\nRunning test...")
            for c in self.local["test"]:
                print("Running %s" % c)
                subprocess.call(c, shell=True)

    def post_default(self, *args, **kwargs):
        pass
