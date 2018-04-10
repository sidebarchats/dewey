import subprocess
from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr

class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        return "printf 'Upgrading dewey... '"

    def run_command(self, *args, **kwargs):
            try:
                with suppress_stdout_stderr():
                    output = subprocess.check_output("/usr/local/bin/pip install git+https://git@github.com/sidebarchats/dewey.git#egg=dewey --upgrade", shell=True,)
                print("complete.")
            except subprocess.CalledProcessError as grepexc:                                                                                                   
                print("\nError upgrading dewey. \n%s" % (grepexc.output,))


    def post_default(self, *args, **kwargs):
        pass
