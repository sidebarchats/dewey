import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr


class Command(DeweyCommand):

    def get_branch_name(self, **kwargs):
        if not hasattr(self, "_branch_name"):
            self._branch_name = kwargs["<branch_name>"]
            if not "feature/" in self._branch_name:
                self._branch_name = "feature/%s" % self._branch_name
        return self._branch_name


    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        branch_name = self.get_branch_name(**kwargs)

        current_branch_cmd = "git rev-parse --abbrev-ref HEAD"
        current_branch = subprocess.check_output(current_branch_cmd, shell=True, )

        puts("")
        puts(colored.green("Creating branch %s" % branch_name))
        puts("")

        base_branch = self.question_with_default("What branch do you want to base the new branch on?", default="master")

        # Checkout master, check if it's behind, ask to pull
        puts("Verifying %s..." % base_branch)
        with indent(4):
            cmd = "git log %s..origin/%s --oneline" % (base_branch, base_branch)
            output = subprocess.check_output(cmd, shell=True, )
            if output == "":
                puts("%s is up to date." % base_branch)
            else:
                puts("%s is behind origin." % base_branch)
                if self.answer_yes_or_no("Do you want to update it?" % base_branch):
                    cmd = "git checkout %s; git pull; git checkout %s" % (base_branch, current_branch)
                    with suppress_stdout_stderr():
                        output = subprocess.check_output(cmd, shell=True, )
                    puts("%s has been updated." % base_branch)
                else:
                    puts("%s has been left alone." % base_branch)
        
        # Start a new branch called feature/foo


        cmd = "git checkout %s; git branch %s" % (base_branch, branch_name)
        with suppress_stdout_stderr():
            output = subprocess.check_output(cmd, shell=True, )

        puts("%s created." % branch_name) 
        # Push it to github
        if self.answer_yes_or_no("Push to github?"):
            cmd = "git push -u origin %s" % (branch_name, )
            with suppress_stdout_stderr():
                output = subprocess.check_output(cmd, shell=True, )
            puts("Pushed.")
        

    def post_default(self, *args, **kwargs):
        # Check out branch
        branch_name = self.get_branch_name(**kwargs)
        return "git checkout %s" % (branch_name,)
