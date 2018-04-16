import os
import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        puts("Checking docker...", newline=False)
        if os.path.isfile("docker-compose.yml"):
            subprocess.call("docker-compose build", shell=True)
            puts(" done.")
        else:
            puts("docker not found.")
            puts("Checking nodejs requirements...", newline=False)
            if os.path.isfile("package.json"):
                puts(" found.")
                puts("Installing package.json...", newline=False)
                subprocess.call("npm install", shell=True)
                puts(" done.")
            else:
                puts(" package.json not found.")

            puts("Checking python requirements...", newline=False)
            if os.path.isfile("requirements.unstable.txt"):
                puts(" found.")
                puts("Installing requirements.unstable.txt...", newline=False)
                subprocess.call("pip install -r requirements.unstable.txt", shell=True)
                puts(" done.")
            elif os.path.isfile("requirements.txt"):
                puts(" found.")
                puts("Installing requirements.txt...", newline=False)
                subprocess.call("pip install -r requirements.txt", shell=True)
                puts(" done.")
            else:
                puts(" no python requirements.txt files found.")

    def post_default(self, *args, **kwargs):
        pass
