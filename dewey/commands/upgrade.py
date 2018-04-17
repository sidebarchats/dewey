import subprocess
from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr

class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        return "printf 'Upgrading dewey... '"

    def run_command(self, *args, **kwargs):
            try:
                with suppress_stdout_stderr():
                    output = subprocess.check_output("bash -c 'pyenv local 3.6.5 && pip install git+https://git@github.com/sidebarchats/dewey.git#egg=dewey --upgrade --force'", shell=True,)
                    output = subprocess.check_output("bash -c 'pyenv local 2.7.7 && pip install git+https://git@github.com/sidebarchats/dewey.git#egg=dewey --upgrade --force'", shell=True,)
                print("complete.")
            except subprocess.CalledProcessError as grepexc:                                                                                                   
                print("\nError upgrading dewey. \n%s" % (grepexc.output,))


    def post_default(self, *args, **kwargs):
        return "source ~/.pyenv/versions/2.7.7/lib/python2.7/site-packages/dewey/bin/bootstrap_dewey.sh"
