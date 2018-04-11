import os
import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr



class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass
        # return 'docker-compose --project-name bu run db bash -c "createdb -h db -U postgres sidebar"'

    def run_command(self, *args, **kwargs):
        if os.path.isfile("package.json"):
            subprocess.call("npm install", shell=True)
        if os.path.isfile("requirements.unstable.txt"):
            subprocess.call("pip install -r requirements.unstable.txt", shell=True)
        elif os.path.isfile("requirements.txt"):
            subprocess.call("pip install -r requirements.txt", shell=True)

    def post_default(self, *args, **kwargs):
        return 'cd app/api; python manage.py migrate'
