from .base import DeweyCommand


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        print("This codebase doesn't appear to support migrate. Check dewey.yml")

    def post_default(self, *args, **kwargs):
        pass
