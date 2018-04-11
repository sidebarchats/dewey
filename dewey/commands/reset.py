import os
import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr


class Command(DeweyCommand):

    def print_section(self, message):
        print("=" * (len(message) + 4))
        print("  %s  " % message)
        print("=" * (len(message) + 4))

    def pre_default(self, *args, **kwargs):
        # print("workon sidebar-core")
        pass

    def run_command(self, *args, **kwargs):
        # Do a full purge & reset of the codebase.
        print("Reset complete.")

    def post_default(self, *args, **kwargs):
        # print("unset PYTHONPATH")
        # print("echo 'Clearing virtualenv'")
        # print("rmvirtualenv sidebar-core")
        # print("mkvirtualenv sidebar-core -p `which python3`")

        # print("echo 'Setting up postactivate'")
        # print("rm ~/.virtualenvs/sidebar-core/bin/postactivate")
        # print("ln -s ~/sidebar/core/postactivate ~/.virtualenvs/sidebar-core/bin/postactivate")
        # print("workon sidebar-core")

        # print("echo 'Installing Python Libraries'")
        # print("workon sidebar-core; pip install -r requirements.txt")
        # print("say Reset done.")
