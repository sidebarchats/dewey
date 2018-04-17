import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        return 'git pull'

    def run_command(self, *args, **kwargs):
        pass

    def post_default(self, *args, **kwargs):
        return '~/.pyenv/versions/2.7.7/lib/python2.7/site-packages/dewey/bin/git-branch-status.sh'
