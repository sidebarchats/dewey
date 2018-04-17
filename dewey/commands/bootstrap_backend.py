import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        puts("Bootstrapping backend...", newline=False)
        subprocess.call("bash -c 'd workon backend; if ! [ -e .setup_run ]; then d setup; fi; docker-compose up -d --no-recreate'", shell=True)
        puts(" done.")

    def post_default(self, *args, **kwargs):
        pass
