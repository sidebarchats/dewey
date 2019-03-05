import os
from .base import DeweyCommand


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        namespace = os.environ.get("DEWEY_ENV", None)
        if namespace is None:
            namespace = "sidebar-"
        else:
            if namespace == "NO_NAMESPACE":
                namespace = ""
            else:
                namespace = "%s-" % namespace

        return "workon %s%s" % (
            namespace,
            kwargs["<app_name>"],
        )

    def run_command(self, *args, **kwargs):
        self.ensure_dev_setup()

    def post_default(self, *args, **kwargs):
        return "export SIDEBAR_USER=%s" % self.brain.username
