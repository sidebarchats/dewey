import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        return "boot2docker init && boot2docker start --vbox-share=disable"

    def run_command(self, *args, **kwargs):
        print("Ready for development")

    def post_default(self, *args, **kwargs):
        pass
