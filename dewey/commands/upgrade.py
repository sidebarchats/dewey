import
import subprocess
from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr

class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        self.venv = False
        if "VIRTUAL_ENV" in os.environ:
            self.venv = os.envrion["VIRTUAL_ENV"].split("/")[-1].replace("sidebar-", "")

        return "printf 'Upgrading dewey... '"

    def run_command(self, *args, **kwargs):
            try:
                with suppress_stdout_stderr():
                    if self.venv:
                        output = subprocess.check_output("deactivate; pip install git+https://git@github.com/sidebarchats/dewey.git#egg=dewey --upgrade --force", shell=True,)
                    else:
                        output = subprocess.check_output("pip install git+https://git@github.com/sidebarchats/dewey.git#egg=dewey --upgrade --force", shell=True,)
                print("complete.")
            except subprocess.CalledProcessError as grepexc:                                                                                                   
                print("\nError upgrading dewey. \n%s" % (grepexc.output,))


    def post_default(self, *args, **kwargs):
        if self.venv:
            return "d workon %s; source ~/.pyenv/versions/2.7/lib/python2.7/site-packages/dewey/bin/bootstrap_dewey.sh" % self.venv
        else:
            return "source ~/.pyenv/versions/2.7/lib/python2.7/site-packages/dewey/bin/bootstrap_dewey.sh"
