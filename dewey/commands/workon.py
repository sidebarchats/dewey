from .base import DeweyCommand

class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        return "workon sidebar-core"

    def run_command(self, *args, **kwargs):
        pass

    def post_default(self, *args, **kwargs):
        return "cd ~/sidebar/core"
