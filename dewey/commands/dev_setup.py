import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        # Make sure we have the user's info.
        self.ensure_dev_setup()

    def post_default(self, *args, **kwargs):
        return "bash <(curl -s https://raw.githubusercontent.com/sidebarchats/meta/master/bootstrap.sh)"
