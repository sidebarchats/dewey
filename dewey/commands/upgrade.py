import subprocess
from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr

class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        return "printf 'Upgrading dewey... '"

    def run_command(self, *args, **kwargs):
            try:
                with suppress_stdout_stderr():
                    output = subprocess.check_output("bash -c 'pip install git+https://git@github.com/sidebarchats/dewey.git#egg=dewey --upgrade' && source ~/.pyenv/versions/2.7/lib/python2.7/site-packages/dewey/bin/bootstrap_dewey.sh", shell=True,)
                print("complete.")
            except subprocess.CalledProcessError as grepexc:                                                                                                   
                print("\nError upgrading dewey. \n%s" % (grepexc.output,))


    def post_default(self, *args, **kwargs):
        pass
