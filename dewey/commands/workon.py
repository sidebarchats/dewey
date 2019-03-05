import os
from .base import DeweyCommand


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        return "workon %s-%s" % (
            os.environ.get("DEWEY_ENV", "sidebar"),
            kwargs["<app_name>"],
        )

    def run_command(self, *args, **kwargs):
        self.ensure_dev_setup()

    def post_default(self, *args, **kwargs):
        return "export SIDEBAR_USER=%s" % self.brain.username
