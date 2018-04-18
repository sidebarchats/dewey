import subprocess
from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr
from clint.textui import puts, indent, colored


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        self.ensure_dev_setup()
        try:
            puts("Upgrading dewey... ", newline=False)
            with suppress_stdout_stderr():
                subprocess.check_output("bash -c 'pyenv local 3.6.5 && pip install git+https://git@github.com/sidebarchats/dewey.git#egg=dewey --upgrade --force'", shell=True,)
                subprocess.check_output("bash -c 'pyenv local 2.7.7 && pip install git+https://git@github.com/sidebarchats/dewey.git#egg=dewey --upgrade --force'", shell=True,)
            puts("complete.")
        except subprocess.CalledProcessError as grepexc:                                                                                                   
            puts("\nError upgrading dewey. \n%s" % (grepexc.output,))


    def post_default(self, *args, **kwargs):
        return "source ~/.pyenv/versions/2.7.7/lib/python2.7/site-packages/dewey/bin/bootstrap_dewey.sh"
