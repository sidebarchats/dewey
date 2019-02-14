from .base import DeweyCommand


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        if self.has_local_override("migrate"):
            return " && ".join(self.local["migrate"])
        else:
            return 'echo "This codebase doesn\'t appear to support migrate. Check dewey.yml"'

    def run_command(self, *args, **kwargs):
        pass

    def post_default(self, *args, **kwargs):
        pass
