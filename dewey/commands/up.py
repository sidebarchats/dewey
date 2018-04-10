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
            ps = subprocess.Popen(
                "gulp dev",
                close_fds=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                cwd="app"
            )
            while ps.poll() is None:
                line = ps.stdout.readline()
                if "[BS] Serving files from: frontends/groundcontrol/build/web" in line:
                    print "Bootstrapping done.  Launching browser."
                    subprocess.check_output("open http://localhost:8111", shell=True,)
                sys.stdout.write(line)
                sys.stdout.flush()
        except KeyboardInterrupt:
            print "\n\nShutting down."

    # def run_command_oliver(self, *args, **kwargs):
    #     try:
    #         ps = subprocess.Popen(
    #             "npm run watch",
    #             close_fds=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    #         )
    #         while ps.poll() is None:
    #             line = ps.stdout.readline()
    #             if "[BS] Serving files from: frontends/groundcontrol/build/web" in line:
    #                 print "Bootstrapping done.  Launching browser."
    #                 subprocess.check_output("open http://localhost:8111", shell=True,)
    #             sys.stdout.write(line)
    #             sys.stdout.flush()
    #     except KeyboardInterrupt:
    #         print "\n\nShutting down."

    def post_default(self, *args, **kwargs):
        pass
